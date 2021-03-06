def correo (name, correo , temaPrincipal, mensaje):

    cadena = """
    <!DOCTYPE html>
<html>
<head>
    <style type="text/css">
        @import url('https://fonts.googleapis.com/css?family=Catamaran:400,800');
        * {
            margin: 0;
            border: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Catamaran', sans-serif;
            background-color: #d8dbdb;
            font-size: 18px;
            max-width: 800px;
            margin: 0 auto;
            padding: 2%;
            color: #565859;
        }
        
        #wrapper {
            background: #f6faff;
        }
        
        img {
            max-width: 100%;
        }
        
        header {
            width: 98%;
        }
        
        #logo {
            max-width: 220px;
            margin: 2% 0 0 5%;
            float: left;
        }
        
        #callout {
            float: right;
            margin: 3% 3% 2% 0;
        }
        
        .social {
            float: right;
            list-style-type: none;
            margin-top: 8%;
        }
        
        .social li {
            display: inline;
        }
        
        .banner {
            margin-bottom: 3%;
        }
        
        .one-col {
            padding: 2%;
        }
        
        h1 {
            letter-spacing: 1%;
        }
        
        p {
            text-align: justify;
        }
        
        .button-holder {
            float: right;
            margin: 0 2% 4% 0;
        }
        
        .btn {
            float: right;
            background: #303840;
            color: #f6faff;
            text-decoration: none;
            font-weight: 800;
            padding: 8px 12px;
            border-radius: 8px;
            letter-spacing: 1px;
        }
        
        .btn:hover {
            background: #58585A;
        }
        
        .line {
            clear: both;
            height: 2px;
            background-color: #e3e9e9;
            margin: 4% auto;
            width: 96%;
        }
        
        .two-col {
            float: left;
            width: 46%;
            padding: 2%;
        }
        
        a {
            color: #607cc3;
            text-decoration: none;
        }
        
        .contact {
            text-align: center;
            padding-bottom: 3%;
        }
        
        @media (max-width: 600px) {
            .two-col {
                width: 97%;
            }
        }
    </style>
</head>

<body>

    <div id="wrapper">
        <header>
            <div id="logo">
                <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/220x60"></a>
            </div>
            <div id="callout">
                <ul class="social">
                    <li>
                        <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/35x35"></a>
                    </li>
                    <li>
                        <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/35x35"></a>
                    </li>
                    <li>
                        <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/35x35"></a>
                    </li>
                    <li>
                        <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/35x35"></a>
                    </li>
                </ul>
            </div>
        </header>

        <div class="banner">
            <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/800x450"></a>
        </div>

        <div class="one-col">
            <h1>HOLAA EQUIPO IOT. Soy """ + str(name) + """</h1>
            <h2>Correo <b>""" + str(correo) + """</b></h2>
            <p>""" + str(temaPrincipal) + """</p>
            <p>""" + str(mensaje) + """</p>
            <div class="button-holder">
                <a class="btn" href="https://responsivehtmlemail.com/" target="_blank">Learn More</a>
            </div>
        </div>

        <div class="line"></div>

        <div class="two-col">
            <h2>Latest Video Release</h2>
            <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/800x450"></a>
            <p>In this months newsletter we'll learn how to design cool email layouts to keep our subscribers and customers informed of new features, services and what they can expect from us in the future to make them happy!</p>
            <a href="https://responsivehtmlemail.com/" target="_blank">Check out the article here...</a>
        </div>

        <div class="two-col">
            <h2>Latest Video Release</h2>
            <a href="https://responsivehtmlemail.com/" target="_blank"><img src="https://via.placeholder.com/800x450"></a>
            <p>In this months newsletter we'll learn how to design cool email layouts to keep our subscribers and customers informed of new features, services and what they can expect from us in the future to make them happy!</p>
            <a href="https://responsivehtmlemail.com/" target="_blank">Check out the article here...</a>
        </div>

        <div class="line"></div>

        <p class="contact">
            Responsive HTML Email<br> (555) 555-5555<br> 1 City Road - Town - State 10000<br>
            <a href="https://responsivehtmlemail.com/" target="_blank">www.responsivehtmlemail.com</a></p>

    </div>
    <!--- End Wrapper -->

</body>

</html>
    """
    return cadena