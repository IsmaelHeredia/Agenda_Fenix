$(document).ready(function () {

    $('#categoriaForm').bootstrapValidator({
        fields: {
            nombre: {
                validators: {
                    notEmpty: {
                        message: 'El nombre es requerido'
                    }
                }
            }
        }
    });

    $('#notaForm').bootstrapValidator({
        fields: {
            titulo: {
                validators: {
                    notEmpty: {
                        message: 'El título es requerido'
                    }
                }
            },
            contenido: {
                validators: {
                    notEmpty: {
                        message: 'El contenido es requerido'
                    }
                }
            },
            categoria: {
                validators: {
                    notEmpty: {
                        message: 'Debe seleccionar una categoria'
                    }
                }
            }
        }
    });

    $('#proyectoForm').bootstrapValidator({
        fields: {
            titulo: {
                validators: {
                    notEmpty: {
                        message: 'El título es requerido'
                    }
                }
            },
            contenido: {
                validators: {
                    notEmpty: {
                        message: 'El contenido es requerido'
                    }
                }
            },
            fecha_inicio: {
                validators: {
                    callback: {
                        callback: function (value, validator, $field) {
                            return true;
                        }
                    }
                }
            },
            fecha_terminado: {
                validators: {
                    callback: {
                        callback: function (value, validator, $field) {
                            return true;
                        }
                    }
                }
            },
            esta_terminado: {
                validators: {
                    callback: {
                        callback: function (value, validator, $field) {
                            return true;
                        }
                    }
                }
            },
        }
    });

    $('#actividadForm').bootstrapValidator({
        fields: {
            titulo: {
                validators: {
                    notEmpty: {
                        message: 'El título es requerido'
                    }
                }
            },
            contenido: {
                validators: {
                    notEmpty: {
                        message: 'El contenido es requerido'
                    }
                }
            },
            fecha: {
                validators: {
                    notEmpty: {
                        message: 'Debe seleccionar una fecha'
                    }
                }
            },
            hora: {
                validators: {
                    callback: {
                        callback: function (value, validator, $field) {
                            return true;
                        }
                    }
                }
            },
            esta_terminado: {
                validators: {
                    callback: {
                        callback: function (value, validator, $field) {
                            return true;
                        }
                    }
                }
            },
        }
    });

    $('#cambiarUsuarioForm').bootstrapValidator({
        fields: {
            usuario: {
                validators: {
                    notEmpty: {
                        message: 'El usuario es requerido'
                    }
                }
            },
            nuevo_usuario: {
                validators: {
                    notEmpty: {
                        message: 'El nuevo usuario es requerido'
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

    $('#cambiarClaveForm').bootstrapValidator({
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
            },
            nueva_clave: {
                validators: {
                    notEmpty: {
                        message: 'La nueva clave es requerida'
                    }
                }
            }
        }
    });

    $('#importarForm').bootstrapValidator({
        fields: {
            directorio: {
                validators: {
                    notEmpty: {
                        message: 'El directorio es requerido'
                    }
                }
            }
        }
    });

    $('#exportarForm').bootstrapValidator({
        fields: {
            directorio: {
                validators: {
                    notEmpty: {
                        message: 'El directorio es requerido'
                    }
                }
            }
        }
    });

});