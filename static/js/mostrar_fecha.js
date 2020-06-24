
let label = $('#fecha_payroll');
let label_hora = $('#hora_payroll');
let fecha = new Date();

label.text(fecha.getFullYear()+'-'+(fecha.getMonth()+1)+'-'+fecha.getDate());

setInterval(cronometro, 1000);

function cronometro() {
    let hora = new Date();
    let minuto = hora.getMinutes();
    if (hora.getMinutes() < 10){
        minuto = '0'+hora.getMinutes();
    }
    label_hora.text(hora.getHours()+':'+minuto+':'+hora.getSeconds());
}


