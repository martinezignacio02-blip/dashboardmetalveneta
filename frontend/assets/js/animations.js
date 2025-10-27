// Animaciones de scroll
document.addEventListener('DOMContentLoaded', function() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                // Remover visible cuando sale de la vista
                entry.target.classList.remove('visible');
            }
        });
    }, observerOptions);

    // Observar todas las secciones con contenido
    const sections = document.querySelectorAll('.section, .content-box');
    sections.forEach(section => {
        section.classList.add('fade-in');
        observer.observe(section);
    });

    // Animación del navbar al hacer scroll
    const navbar = document.querySelector('.navbar');
    const navbarContainer = navbar.querySelector('.container');
    let lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.classList.add('navbar-hidden');
            navbarContainer.classList.add('navbar-logs-only');
        } else {
            navbar.classList.remove('navbar-hidden');
            navbarContainer.classList.remove('navbar-logs-only');
        }
        
        lastScrollTop = scrollTop;
    });

    // Fade out progresivo del hero overlay al hacer scroll
    const heroOverlay = document.querySelector('.hero-overlay');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (heroOverlay) {
            // Calcular opacidad basada en el scroll (0 a 400px)
            const maxScroll = 400;
            const opacity = Math.max(0, 1 - (scrollTop / maxScroll));
            heroOverlay.style.opacity = opacity;
        }
    });

    // Fade out progresivo de los títulos de sección y contenido cuando llegan al header
    const sectionTitles = document.querySelectorAll('.section-title');
    const navbarHeight = 80; // Altura del navbar
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Procesar títulos de sección
        sectionTitles.forEach(title => {
            const rect = title.getBoundingClientRect();
            const distanceToHeader = navbarHeight - rect.top;
            
            // Solo aplicar la animación de fade out si el usuario ha hecho scroll
            if (scrollTop < 100) {
                // No hacer nada si no hay scroll significativo
                return;
            }
            
            // Si el título ya pasó por el header (está por encima), mantenerlo oculto
            if (rect.top < navbarHeight) {
                title.style.opacity = 0;
            } else if (distanceToHeader > 0 && distanceToHeader < 200) {
                // Título está acercándose al header, hacer fade out
                const opacity = Math.max(0, 1 - (distanceToHeader / 200));
                title.style.opacity = opacity;
            } else {
                title.style.opacity = 1;
            }
        });
        
        // Procesar contenido de secciones (texto y gráficos) - desaparece más abajo
        const sections = document.querySelectorAll('.section');
        sections.forEach(section => {
            const content = section.querySelector('p, .content-box, #chart-container');
            if (content) {
                // Solo aplicar la animación si el usuario ha hecho scroll
                if (scrollTop < 100) {
                    return;
                }
                
                const rect = content.getBoundingClientRect();
                const distanceToHeader = navbarHeight - rect.top;
                
                // Si el contenido ya pasó por el header, ocultarlo
                if (rect.top < navbarHeight) {
                    content.style.opacity = 0;
                } else if (distanceToHeader > 0 && distanceToHeader < 200) {
                    // Contenido está acercándose al header, hacer fade out
                    const opacity = Math.max(0, 1 - (distanceToHeader / 200));
                    content.style.opacity = opacity;
                } else {
                    // Contenido está lejos del header, opacidad completa
                    content.style.opacity = 1;
                }
            }
        });
    });
});
