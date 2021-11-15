EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap");

      p,
      h1,
      h2,
      h3,
      h4,
      ol,
      ul,
      li,
      a {
        font-family: Roboto;
        color: #909090;
      }

      body {
        margin: 0px;
        padding: 0px;
      }

      .header {
        display: flex;
        justify-content: center;
        width: 600px;
        height: 120px;
        background-color: #384a6d;
        padding: 0px 40px;
      }

      .header-content {
        display: flex;
        width: 100%;
      }

      .uas-logo {
        width: 80px;
        height: 80px;
        margin-top: 20px;
        margin-left: 400px;
      }

      .uas-date-logo {
        width: 120px;
        height: 120px;
      }

      .title {
        color: #384a6d;
        font-size: 28px;
      }

      .main {
        width: 600px;
        background-color: #ccc;
      }

      .main-content {
        width: 520px;
        margin-top: 16px;
        padding: 0px 40px;
        background-color: #fff;
      }

      p > span {
        font-weight: 700;
      }
    </style>
  </head>
  <body>
    <header class="header">
      <div class="header-content">
        <img
          class="uas-date-logo"
          src="https://res.cloudinary.com/dot7mdnfs/image/upload/v1636952608/UAS_DATE_hmmh5k.png"
          alt="UAS DATE MAIN LOGO"
        />

        <img
          class="uas-logo"
          src="https://res.cloudinary.com/dot7mdnfs/image/upload/v1636953494/UAS-logo_ekahyz.png"
          alt="UAS DATE MAIN LOGO"
        />
      </div>
    </header>
    <main class="main">
      <div class="main-content">
        <h1 class="title">Vicerrectoría</h1>

        <p>Saludos <span>Leonardo Leyva</span>.</p>
        <p>
          Por este medio se le comunica que su solicitud fue revisada por el
          coordinador responsable, el cual ha aceptado su cita.
        </p>
        <p>
          Se le espera en las oficinas del departamento de Servicio Social
          (Vicerrectoría) a la hora seleccionada: <span>11:30</span>
        </p>
      </div>
    </main>
  </body>
</html>
"""
