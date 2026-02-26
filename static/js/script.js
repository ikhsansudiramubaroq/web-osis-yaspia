/**
 * OSIS SMK Website - Main JavaScript
 * Handles all interactive functionality across pages
 */

// Global variables for Gallery Modal to work with inline onclick attributes
let activeGalleryData = [];
let currentImageIndex = 0;

// Global helper functions
function showImage(index) {
  currentImageIndex = index;

  // Lazy check for active data source to support dynamic page loading if needed
  if (activeGalleryData.length === 0) {
    if (document.querySelector(".gallery-grid")) {
      activeGalleryData = fullGalleryData;
    } else {
      activeGalleryData = homeGalleryData;
    }
  }

  updateModalContent();
}

function navigateImage(direction) {
  currentImageIndex += direction;

  // Ensure data is loaded
  if (activeGalleryData.length === 0) {
    if (document.querySelector(".gallery-grid")) {
      activeGalleryData = fullGalleryData;
    } else {
      activeGalleryData = homeGalleryData;
    }
  }

  // Loop logic
  if (currentImageIndex < 0) {
    currentImageIndex = activeGalleryData.length - 1;
  } else if (currentImageIndex >= activeGalleryData.length) {
    currentImageIndex = 0;
  }

  updateModalContent();
}

function updateModalContent() {
  // Gunakan satu variabel saja.
  // Kita pakai homeGalleryData yang dikirim dari Django di index.html
  const data = homeGalleryData[currentImageIndex];

  // Pastikan data ada sebelum mencoba mengakses propertinya
  if (!data) return;

  const modalImage = document.getElementById("modalImage");
  const modalTitle = document.getElementById("modalTitle");
  const modalDesc = document.getElementById("modalDescription");
  const modalDate = document.getElementById("modalDate");

  // Update Gambar
  if (modalImage) {
    modalImage.src = data.src;
    modalImage.alt = data.title;
  }

  // Update Teks (Gunakan || '-' untuk jaga-jaga jika data kosong)
  if (modalTitle) modalTitle.textContent = data.title || "Tanpa Judul";
  if (modalDesc) modalDesc.textContent = data.description || "";
  if (modalDate) modalDate.textContent = data.date || "";

  // Update Views & Likes (Tambahkan default 0 jika data tidak ada di Django)
  if (modalViews) modalViews.textContent = (data.views || "0") + " views";
  if (modalLikes) modalLikes.textContent = (data.likes || "0") + " likes";
}

document.addEventListener("DOMContentLoaded", function () {
  // 1. Initialize AOS (Animate On Scroll)
  // Home page has special offset requirement (-50)
  const isHomePage =
    window.location.pathname.endsWith("index.html") ||
    window.location.pathname.endsWith("/");

  const aosConfig = {
    duration: 600,
    once: true,
    delay: 0,
    easing: "ease-out",
  };

  // Apply specific offset for homepage to assist mobile visibility
  if (isHomePage) {
    aosConfig.offset = -50;
  } else {
    aosConfig.offset = 30;
  }

  AOS.init(aosConfig);

  // 2. Navbar Scroll Effect
  // Adds background to navbar when scrolled
  const navbar = document.getElementById("mainNavbar");
  if (navbar) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
      } else {
        navbar.classList.remove("scrolled");
      }
    });
  }

  // 3. Smooth Scroll for Anchor Links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const href = this.getAttribute("href");
      if (href === "#") return;

      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // 4. Hero Slider (Homepage Only)
  if (document.querySelector(".heroSwiper")) {
    const swiper = new Swiper(".heroSwiper", {
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      effect: "fade",
      fadeEffect: {
        crossFade: true,
      },
    });
  }

  // 5. News Filter & Search (Berita Page)
  const filterButtons = document.querySelectorAll(".filter-btn");
  const newsItems = document.querySelectorAll(".news-item");
  const searchInput = document.getElementById("searchInput");

  if (filterButtons.length > 0 && newsItems.length > 0) {
    // Filter functionality
    filterButtons.forEach((button) => {
      button.addEventListener("click", function () {
        // Remove active class from all buttons
        filterButtons.forEach((btn) => btn.classList.remove("active"));
        // Add active class to clicked button
        this.classList.add("active");

        const filterValue = this.getAttribute("data-filter");

        newsItems.forEach((item) => {
          if (filterValue === "all") {
            showItem(item);
          } else {
            if (item.getAttribute("data-category") === filterValue) {
              showItem(item);
            } else {
              hideItem(item);
            }
          }
        });
      });
    });

    // Search functionality
    if (searchInput) {
      searchInput.addEventListener("keyup", function () {
        const searchValue = this.value.toLowerCase();

        newsItems.forEach((item) => {
          const title = item
            .querySelector(".news-title")
            .textContent.toLowerCase();
          const excerpt = item
            .querySelector(".news-excerpt")
            .textContent.toLowerCase();

          if (title.includes(searchValue) || excerpt.includes(searchValue)) {
            showItem(item);
          } else {
            hideItem(item);
          }
        });
      });
    }
  }

  // 6. Gallery Filter (Galeri Page)
  // Uses logic from #5 but specifically for gallery items
  const galleryItems = document.querySelectorAll(".gallery-item");

  if (document.querySelector(".gallery-grid") && filterButtons.length > 0) {
    filterButtons.forEach((button) => {
      button.addEventListener("click", function () {
        filterButtons.forEach((btn) => btn.classList.remove("active"));
        this.classList.add("active");

        const filterValue = this.getAttribute("data-filter");

        galleryItems.forEach((item) => {
          if (filterValue === "all") {
            showItem(item);
          } else {
            if (item.getAttribute("data-category") === filterValue) {
              showItem(item);
            } else {
              hideItem(item);
            }
          }
        });
      });
    });

    // Setup Active Data for Modal on Load
    activeGalleryData = fullGalleryData;
  } else {
    // On homepage
    activeGalleryData = homeGalleryData;
  }

  // Helper functions for showing/hiding items with animation
  function showItem(item) {
    item.style.display = "block";
    setTimeout(() => {
      item.style.opacity = "1";
      item.style.transform = "scale(1)";
    }, 10);
  }

  function hideItem(item) {
    item.style.opacity = "0";
    item.style.transform = "scale(0.8)";
    setTimeout(() => {
      item.style.display = "none";
    }, 300);
  }

  // 7. Keyboard navigation for modal
  document.addEventListener("keydown", function (e) {
    const modal = document.getElementById("galleryModal");
    // Check if modal exists and is visible (Bootstrap adds 'show' class)
    if (modal && modal.classList.contains("show")) {
      if (e.key === "ArrowLeft") {
        navigateImage(-1);
      } else if (e.key === "ArrowRight") {
        navigateImage(1);
      }
    }
  });
});
