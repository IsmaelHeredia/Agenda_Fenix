
$(document).ready(function() {

    $('[data-toggle="tooltip"]').tooltip();

    $('#dpFecha').datetimepicker({
        locale: 'es',
        format: 'L'
    });

    $('#dpHora').datetimepicker({
        locale: 'es',
        format: 'LT'
    });

    $('#dpFecha_inicio').datetimepicker({
        locale: 'es',
        format: 'L'
    });

    $('#dpFecha_terminado').datetimepicker({
        locale: 'es',
        format: 'L'
    });

    function set_css_file(url){
       var theme = document.getElementById("theme");
       theme.setAttribute("href", "/static/css/" + url);
    }

    $("a[name='sketchy']").click(function(e) {
      
      set_css_file("style_sketchy.css");

      $.ajax({
        type: 'GET',
        url: "/administracion/skins/sketchy",
        data: {},
        dataType: 'json',
        async: false      
      });  

    });

    $("a[name='cursive']").click(function(e) {

      set_css_file("style_cursive.css");

      $.ajax({
        type: 'GET',
        url: "/administracion/skins/cursive",
        data: {},
        dataType: 'json',
        async: false
      });

    });    

    function escribir_textarea(textArea, text) {
        if (textArea.selectionStart || textArea.selectionStart == '0') {
            var startPos = textArea.selectionStart;
            var endPos = textArea.selectionEnd;
            textArea.value = textArea.value.substring(0, startPos)
                + text
                + textArea.value.substring(endPos, textArea.value.length);
            textArea.selectionStart = startPos + text.length;
            textArea.selectionEnd = startPos + text.length;
        } else {
            textArea.value += text;
        }
    }

    $("a[name='agregar_centrar']").click(function(e) {
        var contenido = "[center][/center]";
        var textArea = document.getElementById("id_contenido");
        escribir_textarea(textArea,contenido)
        swal("Agregar Centrado", "Centrado agregado", "success");
        e.preventDefault();
        return false; 
    });

    $("a[name='agregar_negrita']").click(function(e) {
        swal({
          title: "Agregar Negrita",
          text: "",
          type: "input",
          showCancelButton: true,
          confirmButtonText: 'Aceptar',
          cancelButtonText: "Cancelar",
          closeOnConfirm: false,
          inputPlaceholder: "Ingrese texto"
        }, function (texto) {
          if (texto === false) return false;
          if (texto === "") {
            swal.showInputError("Ingrese el texto");
            return false
          }
          var contenido = "[b]"+texto+"[/b]";
          var textArea = document.getElementById("id_contenido");
          escribir_textarea(textArea,contenido)
          swal("Agregar Negrita", "Negrita agregada", "success");
        });
        e.preventDefault();
        return false; 
    });

    $("a[name='agregar_url']").click(function(e) {
        swal({
          title: "Agregar URL",
          text: "",
          type: "input",
          showCancelButton: true,
          confirmButtonText: 'Aceptar',
          cancelButtonText: "Cancelar",
          closeOnConfirm: false,
          inputPlaceholder: "Ingrese url"
        }, function (texto) {
          if (texto === false) return false;
          if (texto === "") {
            swal.showInputError("Ingrese una URL");
            return false
          }
          var contenido = "[url]"+texto+"[/url]";
          var textArea = document.getElementById("id_contenido");
          escribir_textarea(textArea,contenido)
          swal("Agregar URL", "URL agregada", "success");
        });
        e.preventDefault();
        return false; 
    });

    $("a[name='agregar_imagen']").click(function(e) { 
        swal({
          title: "Agregar Imagen",
          text: "",
          type: "input",
          showCancelButton: true,
          confirmButtonText: 'Aceptar',
          cancelButtonText: "Cancelar",
          closeOnConfirm: false,
          inputPlaceholder: "Ingrese link de imagen"
        }, function (texto) {
          if (texto === false) return false;
          if (texto === "") {
            swal.showInputError("Ingrese el link de una imagen");
            return false
          }
          var contenido = "[img]"+texto+"[/img]";
          var textArea = document.getElementById("id_contenido");
          escribir_textarea(textArea,contenido)
          swal("Agregar Imagen", "Imagen agregada", "success");
        });
        e.preventDefault();
        return false; 
    });

    $("a[name='agregar_video']").click(function(e) { 
        swal({
          title: "Agregar Video",
          text: "",
          type: "input",
          showCancelButton: true,
          confirmButtonText: 'Aceptar',
          cancelButtonText: "Cancelar",
          closeOnConfirm: false,
          inputPlaceholder: "Ingrese link de video"
        }, function (texto) {
          if (texto === false) return false;
          if (texto === "") {
            swal.showInputError("Ingrese el link de un video");
            return false
          }
          var contenido = "[video]"+texto+"[/video]";
          var textArea = document.getElementById("id_contenido");
          escribir_textarea(textArea,contenido)
          swal("Agregar Video", "Video agregado", "success");
        });
        e.preventDefault();
        return false; 
    });

    $("a[name='agregar_lista']").click(function(e) { 
        swal({
          title: "Agregar Lista",
          text: "",
          type: "input",
          showCancelButton: true,
          confirmButtonText: 'Aceptar',
          cancelButtonText: "Cancelar",
          closeOnConfirm: false,
          inputPlaceholder: "Ingrese el título de la lista"
        }, function (texto) {
          if (texto === false) return false;
          if (texto === "") {
            swal.showInputError("Ingrese el título de la lista");
            return false
          }
          var contenido = "[lista]\n[titulo]"+texto+"[/titulo]\n[item]test[/item]\n[/lista]";
          var textArea = document.getElementById("id_contenido");
          escribir_textarea(textArea,contenido)
          swal("Agregar Lista", "Lista agregada", "success");
        });
        e.preventDefault();
        return false; 
    });

    $("a[name='agregar_estado']").click(function(e) { 
        var contenido = "[estado=completo]";
        var textArea = document.getElementById("id_contenido");
        escribir_textarea(textArea,contenido)
        swal("Agregar Estado", "Estado agregado", "success");
        e.preventDefault();
        return false; 
    });

    $("a[name='mostrar_comandos']").click(function(e) { 
        swal({
          title: "Comandos",
          text: "Centrado : [center]texto[/center]\nNegrita : [b]texto[/b]\nURL : [url]url[/url]\nImagen : [img]link[/img]\nLista : [lista][titulo]título[/titulo][item]item[/item][/lista]\nEstado : [estado=completo/imcompleto]",
          confirmButtonText: 'Aceptar',
          closeOnConfirm: false
        });
        e.preventDefault();
        return false; 
    });

    var alarma = function() {

      var idata;

      $.ajax({
        type: 'GET',
        url: "/administracion/actividades/comprobar_fechas",
        data: {},
        dataType: 'json',
        async: false,
        success: function(result){idata = result;}
      });

      var respuesta = idata;

      $.each(respuesta, function(index, value) {
          var id = value.pk;
          var titulo = value.fields.titulo;
          var fecha = value.fields.fecha;
          var hora = value.fields.hora

          var hora_split = hora.split(":");
          var horas = hora_split[0];
          var minutos = hora_split[1];

          var hora_limpia = horas + ":" + minutos;

          var contenido = "A las " + hora_limpia + " hs";
          var url = "actividades/leer/" + id;
          toastr.options = {
            "closeButton": true,
            "debug": false,
            "newestOnTop": true,
            "progressBar": false,
            "positionClass": "toast-top-right",
            "preventDuplicates": false,
            "onclick": null,
            "showDuration": "1000",
            "hideDuration": "1000",
            "timeOut": "60000",
            "extendedTimeOut": "1000",
            "showEasing": "swing",
            "hideEasing": "linear",
            "showMethod": "fadeIn",
            "hideMethod": "fadeOut"
          };
          toastr.options.onclick = function () {
            window.location.href = url;
          };
          toastr["success"](contenido, titulo)

          var audioElement = document.createElement("audio");
          audioElement.src = "/static/sounds/analog-alarm-clock.wav"
          audioElement.play();
      });

    };

    var intervalo = 1000 * 60 * 1;

    setInterval(alarma, intervalo);

});

(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();