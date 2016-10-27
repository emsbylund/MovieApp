$(document).ready(function () {
  // Todo: Lägga till enter
  $('#search_form').submit(function(event) {
    search();
    event.preventDefault();
  });
  $('#submit_button').click(search);
});

function search() {
  var search_words = $('#search_words').val(); // Get value from search-box
  var myurl = "http://localhost:8080/search_a_movie/" + encodeURIComponent(search_words);
  $.ajax({
    url: myurl,
    headers: {"Accept": "application/json"}
  }).done(function(data){
    /*console.log(jQuery.isEmptyObject(data));*/
    if (jQuery.isEmptyObject(data) == true){
      no_movie_exists(search_words);
    }else {
      list_movies(data);
    }
  });
};

function list_movies(movies) {
  $('#movie_list').removeClass('hidden');
  if (movies.length == 1) {
    console.log('hej')
    /* Skicka till display_movie() där vi skriver ut HTML-kod för att visa info om film (show_movie.tpl) */
  } else if (movies.length >= 2) {
    $('#movie_list').empty();
    $('#movie_list').append('<ul id="movie_links"></ul>');
    for (i = 0; i < movies.length; i++){
      $('#movie_links').append('<li>' + '<span>' + movies[i]['title'] + '</span>' + ', ' +  '<span>' + movies[i]['year'] + '</span>' + '</li>');
    }
  } else {
    $('#movie_list').empty();
    /* Skriv ut HTML-kod från error.tpl */
  }

  $('#movie_links').children().click( function() {
    var li_elements = $(this).children();
    var title = $(li_elements[0]).text();
    var year = $(li_elements[1]).text();
    get_single_movie(title, year)
  });

}

function get_single_movie(title, year) {
  var url = 'http://localhost:8080/show_movie/' + encodeURIComponent(title) + '/' + encodeURIComponent(year);
  console.log(url);
  $.ajax({
    url: url,
    headers: {"Accept": "application/json"}
  }).done(function(data){
    display_movie(data);
  });
}

function display_movie(movie) {
  $('#movie_list').empty();
  $('#movie_list').append('<h2>' + movie['Title'] + '</h2>');
  $('#movie_list').append('<p>' + movie['Year'] + '</p>');
  $('#movie_list').append('<p>' + movie['Plot'] + '</p>');
  $('#movie_list').append('<p>' + movie['Writer'] + '</p>');
  $('#movie_list').append('<p>' + movie['imdbRating'] + '</p>');
  $('#movie_list').append('<iframe src="' +  movie['youtube_link'] + '"></iframe>');
}

function no_movie_exists(search_words){
  $('#movie_list').removeClass('hidden');
  $('#movie_list').empty();
  $('#movie_list').append('<h2>Hoppsan! Filmen hittades inte! </h2>');
  $('#movie_list').append('<p>Din sökning ' + search_words + ' gav inga resultat.');
}
