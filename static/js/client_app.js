$(document).ready(function () {
   /* Handles the submit button for the search form */
  $('#search_form').submit(function(event) {
    search();
    event.preventDefault();
  });
  $('#submit_button').click(search);
});

function search() {
  /* Gets a list of the movies based on the search-word. */
  var search_words = $('#search_words').val(); // Get value from search-box
  var myurl = "http://localhost:8080/search_a_movie/" + encodeURIComponent(search_words);
  $.ajax({
    url: myurl,
    headers: {"Accept": "application/json"},
    success: function(data) {
      list_movies(data);
    },
    error: function() {
      no_movie_exists(search_words);
    }
  });
};

function list_movies(movies) {
  /* When multible movies excists - presents a list of movies for the user */
  $('#movie_list').removeClass('hidden');
  if (movies.length == 1) {
  } else if (movies.length >= 2) {
    $('#movie_list').empty();
    $('#movie_list').append('<ul id="movie_links"></ul>');
    for (i = 0; i < movies.length; i++){
      $('#movie_links').append('<li>' + '<span>' + movies[i]['title'] + '</span>' + ', ' +  '<span>' + movies[i]['year'] + '</span>' + '</li>');
    }
  } else {
    $('#movie_list').empty();
  }

  $('#movie_links').children().click( function() {
    var li_elements = $(this).children();
    var title = $(li_elements[0]).text();
    var year = $(li_elements[1]).text();
    get_single_movie(title, year)
  });

}

function get_single_movie(title, year) {
  /* Gets information about a single movie */
  var url = 'http://localhost:8080/show_movie/' + encodeURIComponent(title) + '/' + encodeURIComponent(year);
  $.ajax({
    url: url,
    headers: {"Accept": "application/json"}
  }).done(function(data){
    display_movie(data);
  });
}

function display_movie(movie) {
  /* Presents the chosen/searched for movie to the user */
  $('#movie_list').empty();
  $('#movie_list').append('<h2>' + movie['Title'] + '</h2>');
  $('#movie_list').append('<p>' + movie['Year'] + '</p>');
  $('#movie_list').append('<p>' + movie['Plot'] + '</p>');
  $('#movie_list').append('<p>' + movie['Writer'] + '</p>');
  $('#movie_list').append('<p>' + movie['imdbRating'] + '</p>');
  $('#movie_list').append('<iframe src="' +  movie['youtube_link'] + '"></iframe>');
}

function no_movie_exists(search_words){
  /* Presents a error message to the user */
  $('#movie_list').removeClass('hidden');
  $('#movie_list').empty();
  $('#movie_list').append('<h2>Hoppsan! Filmen hittades inte! </h2>');
  $('#movie_list').append('<p>Din sökning ' + search_words + ' gav inga resultat.');
}
