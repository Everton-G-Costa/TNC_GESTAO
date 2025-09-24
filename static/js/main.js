// TNC Gestão - Funcionalidades JavaScript

$(document).ready(function() {
    // Inicializar tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
    
    // Inicializar popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
    
    // Auto-hide alerts após 5 segundos
    setTimeout(function() {
        $('.alert:not(.alert-danger)').fadeOut();
    }, 5000);
    
    // Confirmar exclusão
    $('.btn-delete').on('click', function(e) {
        if (!confirm('Tem certeza que deseja excluir este item?')) {
            e.preventDefault();
        }
    });
    
    // Máscara para CNPJ
    $('input[name="cnpj"]').mask('00.000.000/0000-00');
    
    // Máscara para telefone
    $('input[name="telefone"]').mask('(00) 00000-0000');
    
    // Formatação de moeda
    $('input[type="currency"], .currency').maskMoney({
        prefix: 'R$ ',
        thousands: '.',
        decimal: ',',
        affixesStay: true
    });
    
    // Busca em tempo real
    $('#searchInput').on('keyup', function() {
        var value = $(this).val().toLowerCase();
        $('#dataTable tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    
    // Filtros dinâmicos
    $('.filter-select').on('change', function() {
        updateFilters();
    });
    
    // Atualizar projetos baseado na empresa selecionada
    $('select[name="empresa_id"]').on('change', function() {
        var empresaId = $(this).val();
        var projetoSelect = $('select[name="projeto_id"]');
        
        if (empresaId) {
            $.get('/tnc/api/projetos/' + empresaId, function(data) {
                projetoSelect.empty();
                projetoSelect.append('<option value="">Selecione um projeto</option>');
                
                $.each(data, function(index, projeto) {
                    projetoSelect.append('<option value="' + projeto.id + '">' + projeto.nome + '</option>');
                });
                
                projetoSelect.prop('disabled', false);
            });
        } else {
            projetoSelect.empty();
            projetoSelect.append('<option value="">Selecione uma empresa primeiro</option>');
            projetoSelect.prop('disabled', true);
        }
    });
});

// Funções auxiliares

function updateFilters() {
    var form = $('#filterForm');
    var url = form.attr('action') || window.location.pathname;
    var data = form.serialize();
    
    if (data) {
        window.location.href = url + '?' + data;
    }
}

function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

function formatDate(dateString) {
    var date = new Date(dateString);
    return date.toLocaleDateString('pt-BR');
}

function showLoading(element) {
    var $element = $(element);
    $element.prop('disabled', true);
    $element.html('<span class="loading"></span> Carregando...');
}

function hideLoading(element, originalText) {
    var $element = $(element);
    $element.prop('disabled', false);
    $element.html(originalText);
}

function showAlert(type, message) {
    var alertClass = 'alert-' + (type === 'error' ? 'danger' : type);
    var alertHtml = '<div class="alert ' + alertClass + ' alert-dismissible fade show" role="alert">' +
                   message +
                   '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' +
                   '</div>';
    
    $('.container-fluid').first().prepend(alertHtml);
    
    // Auto-hide after 5 seconds
    setTimeout(function() {
        $('.alert').fadeOut();
    }, 5000);
}

// Funções para gráficos
function createPieChart(canvasId, data, options = {}) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    return new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            var label = context.label || '';
                            var value = context.parsed;
                            var total = context.dataset.data.reduce((a, b) => a + b, 0);
                            var percentage = Math.round((value / total) * 100);
                            
                            return label + ': ' + value + ' (' + percentage + '%)';
                        }
                    }
                }
            },
            ...options
        }
    });
}

function createBarChart(canvasId, data, options = {}) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    return new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            ...options
        }
    });
}

function createLineChart(canvasId, data, options = {}) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    return new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            elements: {
                line: {
                    tension: 0.3
                }
            },
            ...options
        }
    });
}

// Função para exportar dados
function exportTable(format, filename) {
    var table = document.getElementById('dataTable');
    
    if (format === 'csv') {
        var csv = [];
        var rows = table.querySelectorAll('tr');
        
        for (var i = 0; i < rows.length; i++) {
            var row = [];
            var cols = rows[i].querySelectorAll('td, th');
            
            for (var j = 0; j < cols.length; j++) {
                row.push('"' + cols[j].innerText + '"');
            }
            
            csv.push(row.join(','));
        }
        
        downloadCSV(csv.join('\n'), filename);
    }
}

function downloadCSV(csv, filename) {
    var csvFile = new Blob([csv], {type: 'text/csv'});
    var downloadLink = document.createElement('a');
    
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = 'none';
    
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

// Validação de formulários
function validateForm(formId) {
    var form = document.getElementById(formId);
    var inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    var isValid = true;
    
    inputs.forEach(function(input) {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Carregar preferência de dark mode
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}