$(document).ready(function () {

    $('#instalarForm').bootstrapValidator({
        fields: {
            nombre: {
                validators: {
                    notEmpty: {
                        message: 'El nombre es requerido'
                    }
                }
            },
            clave: {
                validators: {
                    notEmpty: {
                        message: 'La clave es requerida'
                    }
                }
            }
        }
    });

    $('#ingresoForm').bootstrapValidator({
        fields: {
            usuario: {
                validators: {
                    notEmpty: {
                        message: 'El usuario es requerido'
                    }
                }
            },
            clave: {
                validators: {
                    notEmpty: {
                        message: 'La clave es requerida'
                    }
                }
            }
        }
    });

});