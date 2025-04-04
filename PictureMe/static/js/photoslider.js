(function() {
	function Slideshow(element) {
		this.el = document.querySelector(element);
		this.init();
	}
	Slideshow.prototype = {
		init: function() {
			this.wrapper = this.el.querySelector(".slider-wrapper");
			this.links = this.el.querySelectorAll("#slider-nav button");
			this.slides = this.el.querySelectorAll(".slide");
			this.previous = this.el.querySelector(".slider-previous");
			this.next = this.el.querySelector(".slider-next");
			this.index = 0;
			this.timer = null;
			this.total = this.slides.length;
			this.actions();
			this.isInit = false;
		},
		_slideTo: function(slide) {
			var currentSlide = this.slides[slide];
			this.wrapper.style.left = "-" + currentSlide.offsetLeft + "px";
			if (this.index === this.total - 1) {
				this.index = this.total - 1;
				this.next.style.display = "none";
			}
			else {
				this.next.style.display = "block";
			}
			if (this.index === 0) {
				this.index = 0;
				this.previous.style.display = "none";
			}
			else {
				this.previous.style.display = "block";
			}
		},
		actions: function() {
		let self = this;
		if (!this.isInit){
		  this.wrapper.style.left = "-" + 0 + "px";
		  this.isInit = true;
		}

		self.next.addEventListener("click", function() {
		  let cur = document.querySelector('#slider-nav button.current')
		  cur.classList.remove('current');
		  self.index++;
		  cur = document.querySelector(`[data-slide="${self.index}"]`);
		  cur.classList.add('current');
		  self._slideTo(self.index);
		}, false);

		self.previous.addEventListener("click", function() {
		  let cur = document.querySelector('#slider-nav button.current')
		  cur.classList.remove('current');
		  self.index--;
		  cur = document.querySelector(`[data-slide="${self.index}"]`);
		  cur.classList.add('current');
		  self._slideTo(self.index);
		}, false);

		document.addEventListener('keydown', function(e) {
		  if (e.key === 'ArrowLeft' || e.keyCode === 37 || e.keyCode === 65) {
		    e.preventDefault();
		    if (self.index > 0) {
		      let cur = document.querySelector('#slider-nav button.current');
		      cur.classList.remove('current');
		      self.index--;
		      let newCur = document.querySelector(`button[data-slide="${self.index}"]`);
		      newCur.classList.add('current');
		      self._slideTo(self.index);
		    }
		  } else if (e.key === 'ArrowRight' || e.keyCode === 39 || e.keyCode === 68) {
		    e.preventDefault();
		    if (self.index < self.total - 1) {
		      let cur = document.querySelector('#slider-nav button.current');
		      cur.classList.remove('current');
		      self.index++;
		      let newCur = document.querySelector(`button[data-slide="${self.index}"]`);
		      newCur.classList.add('current');
		      self._slideTo(self.index);
		    }
		  }
		});


		for (let i = 0; i < self.links.length; i++){
		  self.links[i].addEventListener("click", function() {
			let cur = document.querySelector('#slider-nav button.current')
			cur.classList.remove('current');
			self.links[i].classList.add('current');
			self.index = i;
			self._slideTo(self.index);
		  });
		}

		self.el.addEventListener("touchstart", function(e) {
		  self.touchStartX = e.touches[0].clientX;
		}, false);

		self.el.addEventListener("touchend", function(e) {
		  self.touchEndX = e.changedTouches[0].clientX;
		  // Swipe left: go to next slide if not at the end
		  if (self.touchEndX < self.touchStartX && self.index < self.total - 1) {
		    let cur = document.querySelector('#slider-nav button.current');
		    if(cur) { cur.classList.remove('current'); }
		    self.index++;
		    let newCur = document.querySelector(`button[data-slide="${self.index}"]`);
		    if(newCur) { newCur.classList.add('current'); }
		    self._slideTo(self.index);
		  }
		  // Swipe right: go to previous slide if not at the beginning
		  else if (self.touchEndX > self.touchStartX && self.index > 0) {
		    let cur = document.querySelector('#slider-nav button.current');
		    if(cur) { cur.classList.remove('current'); }
		    self.index--;
		    let newCur = document.querySelector(`button[data-slide="${self.index}"]`);
		    if(newCur) { newCur.classList.add('current'); }
		    self._slideTo(self.index);
		  }
		}, false);


		self.wrapper.addEventListener("click", function(e) {
		  if (e.target.classList.contains("slide")) {
			self.toggleFullScreen();
		  }
		});
	  },

	  toggleFullScreen: function() {
		if (!document.fullscreenElement) {
		  this.el.requestFullscreen();
		} else {
		  if (document.exitFullscreen) {
			document.exitFullscreen();
		  }
		}
	  }
	};

	document.addEventListener("DOMContentLoaded", function() {
		let slider = new Slideshow("#main-slider");
	});
})();
