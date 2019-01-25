// JavaScript Document
$(document).ready(function(){
	//nav_icon
	$("#nav_icon").click(function(){
		if($("nav ul").hasClass( "open" )) $("nav ul").slideUp().removeClass("open");
		else $("nav ul").slideDown().addClass("open");
		/*
		var windowH = $(window).height();
		$("nav").css({'height':($(window).height())+'px'});
		if($("nav").hasClass( "open" )) $("nav").removeClass("open");
		else $("nav").addClass("open");
		*/
	});
	$('#scrollup').click(function(){$("html, body").animate({ scrollTop: 0 }, 1000);});
});
