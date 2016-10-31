<!DOCTYPE html>
<html lang="en">

<head>

	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>MovieApp</title>
	<meta name="description" content="Cardio is a free one page template made exclusively for Codrops by Luka Cvetinovic" />
	<meta name="keywords" content="html template, css, free, one page, gym, fitness, web design" />
	<meta name="author" content="Luka Cvetinovic for Codrops" />
	<!-- Favicons (created with http://realfavicongenerator.net/)-->
	<link rel="apple-touch-icon" sizes="57x57" href="/static/img/favicons/apple-touch-icon-57x57.png">
	<link rel="apple-touch-icon" sizes="60x60" href="/static/img/favicons/apple-touch-icon-60x60.png">
	<link rel="icon" type="image/png" href="/static/img/favicons/favicon-32x32.png" sizes="32x32">
	<link rel="icon" type="image/png" href="/static/img/favicons/favicon-16x16.png" sizes="16x16">
	<link rel="manifest" href="/static/img/favicons/manifest.json">
	<link rel="shortcut icon" href="/static/img/favicons/favicon.ico">
	<meta name="msapplication-TileColor" content="#00a8ff">
	<meta name="msapplication-config" content="/static/img/favicons/browserconfig.xml">
	<meta name="theme-color" content="#ffffff">
	<!-- Normalize -->
	<link rel="stylesheet" type="text/css" href="/static/css/normalize.css">
	<!-- Bootstrap -->
	<link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css">
	<!-- Owl -->
	<link rel="stylesheet" type="text/css" href="/static/css/owl.css">
	<!-- Animate.css -->
	<link rel="stylesheet" type="text/css" href="/static/css/animate.css">
	<!-- Font Awesome -->
	<link rel="stylesheet" type="text/css" href="/static/fonts/font-awesome-4.1.0/css/font-awesome.min.css">
	<!-- Elegant Icons -->
	<link rel="stylesheet" type="text/css" href="/static/fonts/eleganticons/et-icons.css">
	<!-- Main style -->
	<link rel="stylesheet" type="text/css" href="/static/css/cardio.css">
	<link rel="stylesheet" type="text/css" href="/static/css/main.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	<script src="/static/js/client_app.js" type="text/javascript"></script>
</head>

<body>
	<div class="preloader">
		<img src="/static/img/loader.gif" alt="Preloader image">
	</div>
	<header id="intro">
		<div class="container-fluid">
				<div class="row">
					<div class="header-text">
						<div class="col-md-12 text-center col-centered">
							<h2 class="light white">MovieApp</h3>
							<h3 class="light white">- when you just want it simple</h3>
							<h1 class="white typed">It's all about movies...</h1>
							<span class="typed-cursor">|</span>
						</div>
					</div>
				</div>
				<div class="row">
					<section id="wrap" class="col-md-6 offset-md-3">
						<form id="search_form">
							<input type="text" name="search" id="search_words">
							<input type="button" placeholder="Type the movies title here" id="submit_button">
						</form>
					</section>
				</div>
		</div>
	</header>
	<section id="movie_list" class="hidden"></section>

	<section id="team" class="section gray-bg">
		<div class="container">
			<div class="row title text-center">
				<h2 class="margin-top">Team</h2>
				<h4 class="light muted">We're a dream team!</h4>
			</div>
			<div class="row">
			<div class="wraptheteam">
				<div class="col-md-4">
					<div class="team text-center">
						<div class="cover" style="background:url('/static/img/team/team-cover2.jpg'); background-size:cover;">
							<div class="overlay text-center">
								<h3 class="white"></h3>
								<h5 class="light light-white"></h5>
							</div>
						</div>
						<img src="/static/img/team/team1.jpg" alt="Team Image" class="avatar">
						<div class="title">
							<h4>Emma Bylund</h4>
							<h5 class="muted regular">Informationarchitect</h5>
						</div>
					</div>
				</div>
				<div class="col-md-4">
					<div class="team text-center">
						<div class="cover" style="background:url('/static/img/team/team-cover3.jpg'); background-size:cover;">
							<div class="overlay text-center">
								<h3 class="white"></h3>
								<h5 class="light light-white"></h5>
							</div>
						</div>
						<img src="/static/img/team/team2.jpg" alt="Team Image" class="avatar">
						<div class="title">
							<h4>Sofia Lundkvist</h4>
							<h5 class="muted regular">Informationarchitect</h5>
						</div>
					</div>
				</div>
			</div>
		</div>
		</div>
	</section>
	<div class="modal fade" id="modal1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content modal-popup">
				<a href="#" class="close-link"><i class="icon_close_alt2"></i></a>
				<h3 class="white">Sign Up</h3>
				<form action="" class="popup-form">
					<input type="text" class="form-control form-white" placeholder="Full Name">
					<input type="text" class="form-control form-white" placeholder="Email Address">
					<div class="dropdown">
						<button id="dLabel" class="form-control form-white dropdown" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							Pricing Plan
						</button>
						<ul class="dropdown-menu animated fadeIn" role="menu" aria-labelledby="dLabel">
							<li class="animated lightSpeedIn"><a href="#">1 month membership ($150)</a></li>
							<li class="animated lightSpeedIn"><a href="#">3 month membership ($350)</a></li>
							<li class="animated lightSpeedIn"><a href="#">1 year membership ($1000)</a></li>
							<li class="animated lightSpeedIn"><a href="#">Free trial class</a></li>
						</ul>
					</div>
					<div class="checkbox-holder text-left">
						<div class="checkbox">
							<input type="checkbox" value="None" id="squaredOne" name="check" />
							<label for="squaredOne"><span>I Agree to the <strong>Terms &amp; Conditions</strong></span></label>
						</div>
					</div>
					<button type="submit" class="btn btn-submit">Submit</button>
				</form>
			</div>
		</div>
	</div>
	<footer>
		<div class="container">
			<div class="row">
				<div class="col-sm-6 text-center-mobile">
					<h3 class="white">Thanks for checking our page out!</h3>
					<h5 class="light regular light-white">Make sure you come back.</h5>
				</div>
					</div>
				</div>
			</div>
			<div class="row bottom-footer text-center-mobile">
				<div class="col-sm-4 text-right text-center-mobile">
				</div>
			</div>
		</div>
	</footer>
	<!-- Holder for mobile navigation -->
	<div class="mobile-nav">
		<ul>
		</ul>
		<a href="#" class="close-link"><i class="arrow_up"></i></a>
	</div>
	<!-- Scripts -->
	<script src="/static/js/jquery-1.11.1.min.js"></script>
	<script src="/static/js/owl.carousel.min.js"></script>
	<script src="/static/js/bootstrap.min.js"></script>
	<script src="/static/js/wow.min.js"></script>
	<script src="/static/js/typewriter.js"></script>
	<script src="/static/js/jquery.onepagenav.js"></script>
	<script src="/static/js/main.js"></script>
</body>

</html>
