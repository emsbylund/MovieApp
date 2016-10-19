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
      <h2>{{title}}</h2>
      <p>{{year}}</p>
      <h3>Plot</h3>
      <p>{{plot}}</p>
      <p>Författare: {{writer}}</p>
      <iframe src="{{youtube_video_link}}"></iframe>
    </section>
  </body>
</html>
