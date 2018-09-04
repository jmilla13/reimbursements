setInterval(function(){ $$('.fadein img').last().fade({
  duration: .3, afterFinish: function(e){ e.element.remove(); }
}); }, 3000);