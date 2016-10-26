<!DOCTYPE html>
<html>
  <head>
    <title>Filmälskaren</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">
  </head>
  <body>
    <header>
      <h1>Movie App</h1>
    </header>
    <section>
      <h2>Sökresultat</h2>
      <ul>
        %for movie in imdb_list:
          <a href="/show_movie/{{movie['title']}}/{{movie['year']}}"><li>{{movie['title']}}, {{movie['year']}}</li></a>
        % end
      </ul>
    </section>
  </body>
</html>
