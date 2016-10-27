<!DOCTYPE html>
<html>
  <head>
    <title>Filmälskaren</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="/static/js/client_app.js" type="text/javascript"></script>
  </head>
  <body>
    <header>
      <h1>Movie App</h1>
    </header>
    <section>
      <form id="search_form">
        <input type="text" name="search" id="search_words">
        <input type="button" value="Sök" id="submit_button">
      </form>
    </section>
    <section id="movie_list" class="hidden"></section>
  </body>
</html>
