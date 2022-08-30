<html>
    <body>
        <form id="name_form">
            <label>First Name:</label><input type="text" name="first_name"/>
            <br/>
            <label>Last Name:</label><input type="text" name="last_name"/>
            <br/>
            <input type="button" value="enviar" id="envio" name="envio" />
        </form>
        <input type="text" id="resp" name="resp" size="50" /> 

        <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
        <script type="text/javascript">
            $('#envio').click(function(e) {
                    e.preventDefault();

                    if($('[name=first_name]').val().length == 0){
                        $('#resp').val('campo primeiro nome deve ser preenchido');
                        return;
                    }

                    $.ajax({
                        type: 'POST',
                        url: '/api/say_name2',
                        data: $('form').serialize(),
                        success: function(callback) {
                            console.log(callback);
                            $('#resp').val('Ola ' + callback.first_name);
                            $('[name=first_name]').val('');
                        },
                        error: function() {
                            $(this).html("error!");
                        }
                    });
                });
        </script>
    </body>
</html>

