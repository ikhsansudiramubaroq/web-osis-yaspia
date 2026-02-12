/**
 * OSIS SMK Website - Main JavaScript
 * Handles all interactive functionality across pages
 */

// Global variables for Gallery Modal to work with inline onclick attributes
let activeGalleryData = [];
let currentImageIndex = 0;

// Homepage Preview Data (Subset)
const homeGalleryData = [
    {
        src: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=800&h=800&fit=crop',
        title: 'Pelantikan OSIS 2025/2026',
        description: 'Pelantikan pengurus OSIS periode baru dilaksanakan dengan khidmat di aula sekolah. Acara dihadiri oleh Kepala Sekolah, para guru, dan seluruh siswa.',
        date: '10 Feb 2026',
        views: '1,234',
        likes: '89'
    },
    {
        src: 'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=800&h=800&fit=crop',
        title: 'Seminar Motivasi',
        description: 'OSIS menghadirkan motivator muda untuk memberikan seminar tentang bagaimana meraih kesuksesan di era digital kepada seluruh siswa.',
        date: '08 Feb 2026',
        views: '987',
        likes: '65'
    },
    {
        src: 'https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?w=800&h=800&fit=crop',
        title: 'Lomba Debat Antar Kelas',
        description: 'Kompetisi debat bahasa Indonesia tingkat SMK se-kota berlangsung seru dengan partisipasi aktif dari semua kelas.',
        date: '05 Feb 2026',
        views: '856',
        likes: '54'
    },
    {
        src: 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=800&h=800&fit=crop',
        title: 'Workshop Public Speaking',
        description: 'Kegiatan workshop public speaking diadakan untuk meningkatkan kemampuan berkomunikasi anggota OSIS di depan umum.',
        date: '03 Feb 2026',
        views: '745',
        likes: '48'
    },
    {
        src: 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800&h=800&fit=crop',
        title: 'Study Tour Museum',
        description: 'Kegiatan study tour dilaksanakan untuk menambah wawasan siswa tentang sejarah dan budaya Indonesia di Museum Nasional.',
        date: '01 Feb 2026',
        views: '1,102',
        likes: '72'
    },
    {
        src: 'https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=800&h=800&fit=crop',
        title: 'Lomba Tari Tradisional',
        description: 'Tim kesenian OSIS berhasil meraih juara harapan dalam lomba tari tradisional tingkat kota dengan membawakan tari Saman.',
        date: '28 Jan 2026',
        views: '1,456',
        likes: '98'
    }
];

// Full Gallery Page Data (Superset)
const fullGalleryData = [
    ...homeGalleryData, // Include home data first
    // Add unique items from gallery page
    {
        src: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1200&h=800&fit=crop',
        title: 'Upacara Bendera',
        description: 'Upacara bendera rutin setiap hari Senin dengan khidmat.',
        date: '05 Feb 2026',
        views: '678',
        likes: '234'
    },
    {
        src: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=1200&h=800&fit=crop',
        title: 'Juara Karya Tulis Ilmiah',
        description: 'Prestasi membanggakan meraih juara pertama lomba KTI tingkat provinsi.',
        date: '08 Feb 2026',
        views: '1,523',
        likes: '789'
    },
    {
        src: 'https://images.unsplash.com/photo-1559027615-cd4628902d4a?w=1200&h=800&fit=crop',
        title: 'Bakti Sosial Panti Asuhan',
        description: 'Kegiatan sosial berbagi kasih di panti asuhan setempat.',
        date: '05 Feb 2026',
        views: '1,289',
        likes: '645'
    },
    {
        src: 'https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=800&fit=crop',
        title: 'Program Penghijauan',
        description: 'Menanam 100 pohon untuk lingkungan sekolah yang lebih asri.',
        date: '28 Jan 2026',
        views: '823',
        likes: '412'
    },
    {
        src: 'https://images.unsplash.com/photo-1529070538774-1843cb3265df?w=1200&h=800&fit=crop',
        title: 'Turnamen Futsal',
        description: 'Kompetisi futsal antar kelas yang berlangsung meriah dan seru.',
        date: '01 Feb 2026',
        views: '1,678',
        likes: '834'
    },
    {
        src: 'https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?w=1200&h=800&fit=crop',
        title: 'Pelatihan Kepemimpinan',
        description: 'Workshop pengembangan softskill dan kepemimpinan bagi pengurus OSIS.',
        date: '28 Feb 2026',
        views: '967',
        likes: '523'
    },
    {
        src: 'https://images.unsplash.com/photo-1544531586-fde5298cdd40?w=1200&h=800&fit=crop',
        title: 'Donor Darah PMI',
        description: 'Kegiatan donor darah bersama PMI untuk membantu sesama.',
        date: '20 Feb 2026',
        views: '1,134',
        likes: '589'
    },
    {
        src: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200&h=800&fit=crop',
        title: 'Rapat Koordinasi OSIS',
        description: 'Rapat koordinasi pengurus OSIS membahas program kerja semester ini.',
        date: '12 Feb 2026',
        views: '543',
        likes: '267'
    },
    {
        src: 'https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=1200&h=800&fit=crop',
        title: 'Pentas Musik Akustik',
        description: 'Penampilan musik akustik dari siswa-siswi berbakat.',
        date: '18 Feb 2026',
        views: '1,423',
        likes: '712'
    },
    {
        src: 'https://images.unsplash.com/photo-1543269865-cbf427effbad?w=1200&h=800&fit=crop',
        title: 'Kompetisi Basket',
        description: 'Pertandingan basket sengit antar kelas dalam rangka class meeting.',
        date: '22 Jan 2026',
        views: '1,234',
        likes: '678'
    },
    {
        src: 'https://images.unsplash.com/photo-1533929736458-ca588d08c8be?w=1200&h=800&fit=crop',
        title: 'Pameran Karya Siswa',
        description: 'Pameran hasil karya siswa dari berbagai bidang keahlian.',
        date: '30 Jan 2026',
        views: '989',
        likes: '534'
    },
    {
        src: 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=1200&h=400&fit=crop',
        title: 'Team Building OSIS',
        description: 'Kegiatan team building untuk mempererat kebersamaan pengurus OSIS.',
        date: '17 Feb 2026',
        views: '867',
        likes: '445'
    }
];

// Global helper functions
function showImage(index) {
    currentImageIndex = index;

    // Lazy check for active data source to support dynamic page loading if needed
    if (activeGalleryData.length === 0) {
        if (document.querySelector('.gallery-grid')) {
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
        if (document.querySelector('.gallery-grid')) {
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
    if (!activeGalleryData[currentImageIndex]) return;

    const data = activeGalleryData[currentImageIndex];
    const modalImage = document.getElementById('modalImage');
    const modalTitle = document.getElementById('modalTitle');
    const modalDesc = document.getElementById('modalDescription');
    const modalDate = document.getElementById('modalDate');
    const modalViews = document.getElementById('modalViews');
    const modalLikes = document.getElementById('modalLikes');

    if (modalImage) {
        modalImage.src = data.src;
        modalImage.alt = data.title;
    }
    if (modalTitle) modalTitle.textContent = data.title;
    if (modalDesc) modalDesc.textContent = data.description;
    if (modalDate) modalDate.textContent = data.date;
    if (modalViews) modalViews.textContent = data.views + ' views';
    if (modalLikes) modalLikes.textContent = data.likes + ' likes';
}

document.addEventListener('DOMContentLoaded', function () {
    // 1. Initialize AOS (Animate On Scroll)
    // Home page has special offset requirement (-50)
    const isHomePage = window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('/');

    const aosConfig = {
        duration: 600,
        once: true,
        delay: 0,
        easing: 'ease-out'
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
    const navbar = document.getElementById('mainNavbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // 3. Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 4. Hero Slider (Homepage Only)
    if (document.querySelector('.heroSwiper')) {
        const swiper = new Swiper('.heroSwiper', {
            loop: true,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            effect: 'fade',
            fadeEffect: {
                crossFade: true
            },
        });
    }

    // 5. News Filter & Search (Berita Page)
    const filterButtons = document.querySelectorAll('.filter-btn');
    const newsItems = document.querySelectorAll('.news-item');
    const searchInput = document.getElementById('searchInput');

    if (filterButtons.length > 0 && newsItems.length > 0) {
        // Filter functionality
        filterButtons.forEach(button => {
            button.addEventListener('click', function () {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                // Add active class to clicked button
                this.classList.add('active');

                const filterValue = this.getAttribute('data-filter');

                newsItems.forEach(item => {
                    if (filterValue === 'all') {
                        showItem(item);
                    } else {
                        if (item.getAttribute('data-category') === filterValue) {
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
            searchInput.addEventListener('keyup', function () {
                const searchValue = this.value.toLowerCase();

                newsItems.forEach(item => {
                    const title = item.querySelector('.news-title').textContent.toLowerCase();
                    const excerpt = item.querySelector('.news-excerpt').textContent.toLowerCase();

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
    const galleryItems = document.querySelectorAll('.gallery-item');

    if (document.querySelector('.gallery-grid') && filterButtons.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function () {
                filterButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');

                const filterValue = this.getAttribute('data-filter');

                galleryItems.forEach(item => {
                    if (filterValue === 'all') {
                        showItem(item);
                    } else {
                        if (item.getAttribute('data-category') === filterValue) {
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
        item.style.display = 'block';
        setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'scale(1)';
        }, 10);
    }

    function hideItem(item) {
        item.style.opacity = '0';
        item.style.transform = 'scale(0.8)';
        setTimeout(() => {
            item.style.display = 'none';
        }, 300);
    }

    // 7. Keyboard navigation for modal
    document.addEventListener('keydown', function (e) {
        const modal = document.getElementById('galleryModal');
        // Check if modal exists and is visible (Bootstrap adds 'show' class)
        if (modal && modal.classList.contains('show')) {
            if (e.key === 'ArrowLeft') {
                navigateImage(-1);
            } else if (e.key === 'ArrowRight') {
                navigateImage(1);
            }
        }
    });

});
