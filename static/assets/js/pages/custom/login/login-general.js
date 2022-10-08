// localStorage.removeItem('session_key');
// localStorage.removeItem('session_refresh');
"use strict";

// Class Definition
var KTLogin = function () {
    var _login;

    var _showForm = function (form) {
        var cls = 'login-' + form + '-on';
        var form = 'kt_login_' + form + '_form';

        _login.removeClass('login-signin-on');

        _login.addClass(cls);

        KTUtil.animateClass(KTUtil.getById(form), 'animate__animated animate__backInUp');
    }

    var _handleSignInForm = function () {
        var validation;

        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validation = FormValidation.formValidation(
            KTUtil.getById('kt_login_signin_form'),
            {
                fields: {
                    username: {
                        validators: {
                            notEmpty: {},
                        }
                    },
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    submitButton: new FormValidation.plugins.SubmitButton(),
                    //defaultSubmit: new FormValidation.plugins.DefaultSubmit(), // Uncomment this line to enable normal button submit after form validation
                    bootstrap: new FormValidation.plugins.Bootstrap()
                }
            }
        );
        $('#kt_login_signin_form').on('submit', function (e) {
            e.preventDefault();
            validation.validate().then(function (status) {
                console.log(status)
                if (status === 'Valid') {
                    console.log('SENDING')
                    document.getElementById('kt_login_signin_submit').className = 'spinner pl-15 spinner-track spinner-dark spinner-left btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-3'
                    $.ajax({
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        method: 'POST',
                        url: "/api/v1/auth/login/",
                        data: JSON.stringify({
                            dashboard_login: 1,
                            username: document.querySelector('#kt_login_signin_form input[name=username]').value,
                            password: document.querySelector('#kt_login_signin_form input[name=password]').value,
                        }),
                        success: function (res) {
                            if (res["access"]) {
                                localStorage.setItem('session_key', 'Bearer ' + res["access"]);
                                localStorage.setItem('session_refresh', res["refresh"]);
                                window.open('/dashboard', '_self');
                            } else {
                                toastrFireSuccess(res["detail"]);
                                _showForm('login-code');
                                document.getElementById('kt_login_signin_submit').className = 'btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-3'
                            }
                        },
                        error: function (res) {
                            console.log(res)
                            if (res['status'] === 401) {
                                swalFireError('Invalid username or password!');
                                document.getElementById('kt_login_signin_submit').className = 'btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-3'

                            } else {
                                swalFireError('Some Error happened! try again');
                                document.getElementById('kt_login_signin_submit').className = 'btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-3'

                            }
                        }
                    });
                } else {

                    swal.fire({
                        text: "There is some error!",
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: "ok",
                        customClass: {
                            confirmButton: "btn font-weight-bold btn-light-primary"
                        }
                    }).then(function () {
                        KTUtil.scrollTop();
                    });
                }
            });
        });
    }

    var _handleLoginCodeForm = function (e) {
        var validation;

        console.log('HERE')
        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validation = FormValidation.formValidation(
            KTUtil.getById('kt_login_login-code_form'),
            {
                fields: {
                    login_code: {
                        validators: {
                            notEmpty: {
                                message: 'وارد کردن کد تایید اجباری است'
                            }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap: new FormValidation.plugins.Bootstrap()
                }
            }
        );

        // Handle submit button
        $('#kt_login_login-code_form').on('submit', function (e) {
            e.preventDefault();
            console.log('HERE')

            validation.validate().then(function (status) {
                console.log('HERE')
                if (status == 'Valid') {
                    console.log('HERE')
                    document.getElementById('kt_login_login-code_submit').className = 'btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-4 spinner pl-15 spinner-track spinner-dark spinner-left';
                    $.ajax({
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        method: 'POST',
                        url: "/api/v1/auth/login/",
                        data: JSON.stringify({
                            username: document.querySelector('#kt_login_signin_form input[name=email]').value,
                            password: document.querySelector('#kt_login_signin_form input[name=email]').value,
                        }),
                        success: function (res) {
                            localStorage.setItem('session_key', 'Bearer ' + res["access"]);
                            localStorage.setItem('session_refresh', res["refresh"]);
                            window.open('/dashboard', '_self');
                        },
                        error: function (res) {
                            swalFireError('کد وارد شده صحیح نمی باشد! لطفا دوباره تلاش کنید!');
                            document.getElementById('kt_login_login-code_submit').className = 'btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-3'
                        }
                    });
                } else {
                    swal.fire({
                        text: "تعدادی خطا وجود دارد! لطفا دوباره تلاش کنید!",
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: "i got that",
                        customClass: {
                            confirmButton: "btn font-weight-bold btn-light-primary"
                        }
                    }).then(function () {
                        KTUtil.scrollTop();
                    });
                }
            });
        });


        // Handle cancel button
        $('#kt_login_login-code_cancel').on('click', function (e) {
            e.preventDefault();
            _showForm('signin');
        });


        // Handle cancel button
        $('#kt_login_register-code_cancel').on('click', function (e) {
            e.preventDefault();

            _showForm('register-code');
        });
    }
    // Public Functions
    return {
        // public functions
        init: function () {
            _login = $('#kt_login');
            console.log('LIG')
            _handleSignInForm();
            // _handleLoginCodeForm();
        }
    };
}();

// Class Initialization
