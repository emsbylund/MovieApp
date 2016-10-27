/*$(document).ready(function () {
  console.log("JQuery funkar!");  // Skriver ut en text till konsollen.
});*/

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
  console.log(myurl);
  $.ajax({
    url: myurl,
    headers: {"Accept": "application/json"}
  }).done(function(data){
    list_movies(data);
  });
};

function list_movies(movies) {
  console.log(movies);
  $('#movie_list').removeClass('hidden');
  if (movies.length == 1) {
    console.log('hej')
    /* Skriv ut HTML-kod från show_result.tpl */
  } else if (movies.length >= 2) {
    /* Skriv ut HTML-kod från list_movies.tpl.
    Loopa igenom listan med filmer, skriv li för varje. */
    $('#movie_list').append('<ul id="movie_links"></ul>');
    for (i = 0; i < movies.length; i++){
      $('#movie_links').append('<li>' + '<span>' + movies[i]['title'] + '</span>' + ', ' +  '<span>' + movies[i]['year'] + '<span>' + '</li>');
    }
      /*$('#movie_list').append('</ul>');*/
  } else {
    console.log('hejhej')
    /* Skriv ut HTML-kod från error.tpl */
  }

  console.log($('#movie_links').each());
  /*$('#movie_links li').each().click(function() {
    console.log($(this).find('span').html());
  });*/
}

function display_movie() {


}
