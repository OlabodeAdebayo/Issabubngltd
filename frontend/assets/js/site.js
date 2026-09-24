const RAILWAY_PUBLIC_API = 'https://issabubngltd-production.up.railway.app/api';
const LOCAL_API = ['localhost','127.0.0.1'].includes(window.location.hostname) ? 'http://127.0.0.1:8000/api' : '/api';
const API_BASE = (window.ISSABUB_API_BASE || LOCAL_API).replace(/\/$/, '');

const servicesFallback = [
 {number:'01',title:'Technical Sub-Contracting',slug:'technical-sub-contracting',description:'Specialized labor, skilled manpower and execution support for large-scale industrial and EPC projects.',image:'assets/images/service-technical.jpg',benefits:['Access to skilled technical personnel','Rapid mobilization and flexible workforce scaling','Industrial and EPC execution support','Safety, quality and schedule discipline'],applications:'Industrial plants, EPC project execution and site works, oil & gas, power, mining, manufacturing, shutdowns and structural erection.'},
 {number:'02',title:'Mechanical Engineering',slug:'mechanical-engineering',description:'Design, analysis and engineering support for mechanical systems and equipment, including fabrication, installation and commissioning.',image:'assets/images/service-mechanical.jpg',benefits:['Expert design and engineering analysis','Mechanical systems and equipment support','Fabrication and precision manufacturing','Technical support and optimization'],applications:'Industrial machinery, production equipment, piping, HVAC, process equipment and EPC mechanical installations.'},
 {number:'03',title:'Industrial Maintenance',slug:'industrial-maintenance',description:'Scheduled and emergency maintenance services for industrial facilities, machinery and critical systems to reduce downtime and extend asset life.',image:'assets/images/service-maintenance.jpg',benefits:['Preventive maintenance programs','Emergency repair and breakdown support','Experienced industrial technicians','Maintenance reporting and compliance'],applications:'Manufacturing plants, machinery, shutdowns, turnarounds, pumps, conveyors, boilers and process equipment.'},
 {number:'04',title:'Building & Construction',slug:'building-construction',description:'Complete building construction from groundwork and foundations through structural works, finishing and handover.',image:'assets/images/service-construction.jpg',benefits:['End-to-end project management','Site engineering supervision','Quality and timeline control','Safety and regulatory compliance'],applications:'Residential homes, estates, apartments, offices, shops, warehouses, factories, schools, hospitals, extensions and refurbishments.'}
];
const projectsFallback = [
 ['Retail Shopping Centre Expansion','commercial','Expansion of an existing shopping centre adding 2,800 sqm of new retail and food-court space. The scope includes structural works, external envelope, public plazas and integration with existing systems.','assets/images/project-retail.jpg'],
 ['Office Building Shell & Core','commercial','Construction of a four-storey commercial office building of approximately 3,200 sqm, including structural frame, façade, core services and base-build systems.','assets/images/project-office-shell.jpg'],
 ['Commercial Warehouse Frame','commercial','Full structural steel framework for a 1,200 sqm warehouse including columns, beams, purlins, wall girts, bracing, base plates and connections.','assets/images/project-warehouse.jpg'],
 ['Apartment Fit-Out & Interiors','residential','Complete interior fit-out of a 12-unit residential apartment block including kitchens, bathrooms, flooring, joinery, ceilings, lighting, plumbing and electrical works.','assets/images/project-apartment.jpg'],
 ['Townhouse Development','residential','Turnkey construction of an eight-unit contemporary townhouse development with private courtyards, parking, modern interiors and shared landscaped areas.','assets/images/project-townhouse.jpg'],
 ['Family Home Extension & Remodel','residential','Major rear extension and internal remodel involving structural modifications, new living areas, upgraded bathrooms and integrated finishes.','assets/images/project-family.jpg'],
 ['Clinker Transport System Repair','retrofitting','Comprehensive repair and rehabilitation of a clinker transport system including structural assessment, frame strengthening, steel replacement, conveyor support repair and safety systems.','assets/images/project-clinker.jpg'],
 ['Industrial Facility Upgrade','retrofitting','Retrofitting of an existing industrial building including structural strengthening, roof replacement, cladding upgrades, insulation and mechanical/electrical modernisation.','assets/images/project-industrial-upgrade.jpg'],
 ['Office Space Refurbishment','retrofitting','Complete interior renovation of a commercial office floor with partitions, suspended ceilings, raised flooring, lighting, HVAC, electrical and data installations.','assets/images/project-office-refurbishment.jpg'],
 ['Sports Arena Roof Truss','structural','Long-span steel space-frame roof structure spanning 80 metres for an indoor multi-purpose arena, including trusses, purlins, bracing and access walkways.','assets/images/project-arena.jpg'],
 ['Integration of Existing Cement Silo','structural','Integration of an existing cement silo with a new process line through steelwork, platforms, access structures and connections.','assets/images/project-silo.jpg'],
 ['Industrial Portal Frame Building','structural','Design, fabrication and erection of a large-span steel portal frame for a manufacturing facility supporting crane runway beams, heavy equipment loads and access platforms.','assets/images/project-portal.jpg']
].map(([title,category,description,image])=>({title,category,description,image}));

const categoryLabels = {commercial:'Commercial',residential:'Residential',retrofitting:'Retrofitting & Restoration',structural:'Structural Steel'};
const esc = value => String(value ?? '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));

function header(){
 const host=document.getElementById('site-header'); if(!host)return;
 const current=location.pathname.split('/').pop()||'index.html';
 host.innerHTML=`<a class="skip-link" href="#main-content">Skip to content</a><header class="site-header"><a class="brand" href="index.html" aria-label="ISSABUB Nigeria Limited home"><img src="assets/images/logo.png" alt="ISSABUB Nigeria Limited logo"><span class="brand-name">ISSABUB NIGERIA LIMITED</span></a><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button><nav id="site-nav" class="site-nav" aria-label="Primary navigation"><a data-page="index.html" href="index.html">Home</a><a data-page="about.html" href="about.html">About</a><a data-page="services.html" href="services.html">Services</a><a data-page="projects.html" href="projects.html">Projects</a><a data-page="contact.html" href="contact.html">Contact</a><a class="nav-cta" href="contact.html#quote">Secure Quote</a></nav></header>`;
 document.querySelectorAll('.site-nav a[data-page]').forEach(a=>{if(a.dataset.page===current)a.setAttribute('aria-current','page');a.addEventListener('click',closeMenu)});
 const toggle=document.querySelector('.nav-toggle'); toggle?.addEventListener('click',()=>{const nav=document.querySelector('.site-nav');const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));document.body.classList.toggle('menu-open',open)});
}
function closeMenu(){document.querySelector('.site-nav')?.classList.remove('open');document.querySelector('.nav-toggle')?.setAttribute('aria-expanded','false');document.body.classList.remove('menu-open')}
function footer(){const host=document.getElementById('site-footer');if(!host)return;host.innerHTML=`<footer class="footer"><div class="container footer-grid"><div><a class="brand" href="index.html"><img src="assets/images/logo.png" alt="ISSABUB logo"><span>ISSABUB NIGERIA LIMITED</span></a><p>Your vision, our execution.</p><p>Established construction and civil engineering contractor in Ogun State, Nigeria.</p></div><div><h3>Quick Links</h3><a href="index.html">Home</a><a href="about.html">About Us</a><a href="services.html">Services</a><a href="projects.html">Projects</a><a href="contact.html">Contact</a></div><div><h3>Services</h3><span>Technical Sub-Contracting</span><span>Mechanical Engineering</span><span>Industrial Maintenance</span><span>Building &amp; Construction</span></div><div><h3>Business Hours</h3><span>Monday–Friday: 8 AM–6 PM</span><span>Saturday: 8 AM–3 PM</span><span>Sunday: Closed</span><p><a href="tel:+2348126843284">+234 812 684 3284</a><a href="mailto:issabubngltd@outlook.com">issabubngltd@outlook.com</a></p></div></div><div class="container footer-bottom"><span>© 2026 ISSABUB Nigeria Limited. All rights reserved.</span><span>15, Kajola Estate, Ifelodun Street, Off Gasline, Ijoko Ota, Ogun State.</span></div></footer>`}
function serviceCard(s){return `<article class="service-card" style="background-image:url('${esc(s.image)}')"><span class="tag">Service ${esc(s.number)}</span><h3>${esc(s.title)}</h3><p>${esc(s.description)}</p><a class="text-link" href="services.html">Learn more →</a></article>`}
function projectCard(p,index){const label=categoryLabels[p.category]||p.category||'Project';return `<article class="project-card"><div class="project-media"><img src="${esc(p.image)}" alt="${esc(p.title)}" loading="lazy" decoding="async"><button class="project-zoom" type="button" data-project-index="${index}" aria-label="View larger image of ${esc(p.title)}">↗</button></div><div class="project-body"><span class="tag">${esc(label)}</span><h3>${esc(p.title)}</h3><p>${esc(p.description)}</p></div></article>`}
function renderServices(list,target){if(!target)return;target.innerHTML=list.map(serviceCard).join('');const select=document.getElementById('service-select');if(select)select.innerHTML='<option value="">Select a service</option>'+list.map(s=>`<option value="${esc(s.title)}">${esc(s.title)}</option>`).join('')}
function renderServiceDetails(list){const target=document.getElementById('service-list');if(!target)return;target.innerHTML=list.map(s=>`<article class="service-detail"><div><p class="eyebrow">SERVICE ${esc(s.number)}</p><h2>${esc(s.title)}</h2><p>${esc(s.description)}</p><h3>Key Benefits</h3><ul class="benefits">${(s.benefits||[]).map(x=>`<li>${esc(x)}</li>`).join('')}</ul><h3>Typical Applications</h3><p>${esc(s.applications)}</p><a class="btn btn-primary" href="contact.html#quote">Request a Quote</a></div><img class="service-detail-img" src="${esc(s.image)}" alt="${esc(s.title)}" loading="lazy" decoding="async"></article>`).join('')}
function renderProjects(list,target){if(!target)return;target.innerHTML=list.length?list.map((p,i)=>projectCard(p,i)).join(''):`<div class="empty-state">No projects are available in this category yet.</div>`;target.querySelectorAll('.project-zoom').forEach(btn=>btn.addEventListener('click',()=>openProjectModal(list[Number(btn.dataset.projectIndex)])))}
function ensureModal(){if(document.getElementById('project-modal'))return;const m=document.createElement('div');m.id='project-modal';m.className='modal';m.setAttribute('aria-hidden','true');m.innerHTML='<div class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="modal-title"><button class="modal-close" type="button" aria-label="Close project image">×</button><img id="modal-image" alt=""><div class="modal-content"><span id="modal-category" class="tag"></span><h2 id="modal-title"></h2><p id="modal-description"></p></div></div>';document.body.appendChild(m);m.addEventListener('click',e=>{if(e.target===m||e.target.closest('.modal-close'))closeProjectModal()});document.addEventListener('keydown',e=>{if(e.key==='Escape')closeProjectModal()})}
function openProjectModal(p){if(!p)return;ensureModal();const m=document.getElementById('project-modal');document.getElementById('modal-image').src=p.image;document.getElementById('modal-image').alt=p.title;document.getElementById('modal-category').textContent=categoryLabels[p.category]||p.category||'Project';document.getElementById('modal-title').textContent=p.title;document.getElementById('modal-description').textContent=p.description;m.classList.add('open');m.setAttribute('aria-hidden','false');document.body.classList.add('menu-open');document.querySelector('.modal-close')?.focus()}
function closeProjectModal(){const m=document.getElementById('project-modal');if(!m)return;m.classList.remove('open');m.setAttribute('aria-hidden','true');document.body.classList.remove('menu-open')}
async function api(path,fallback){try{const controller=new AbortController();const timer=setTimeout(()=>controller.abort(),6500);const r=await fetch(`${API_BASE}/${path}`,{headers:{Accept:'application/json'},signal:controller.signal});clearTimeout(timer);if(!r.ok)throw new Error(`API ${r.status}`);const d=await r.json();return d.results||d}catch(error){console.warn('ISSABUB API fallback:',error);return fallback}}
async function boot(){header();footer();const [services,projects]=await Promise.all([api('services/',servicesFallback),api('projects/',projectsFallback)]);const normalizedProjects=(projects||projectsFallback).map((p,i)=>({...p,image:p.image||projectsFallback[i]?.image||projectsFallback[0].image}));renderServices(services,document.getElementById('home-services'));renderServiceDetails(services);const homeProjects=document.getElementById('home-projects');renderProjects(normalizedProjects.slice(0,6),homeProjects);const projectList=document.getElementById('project-list');renderProjects(normalizedProjects,projectList);const filters=document.querySelectorAll('.filter');filters.forEach(btn=>btn.addEventListener('click',()=>{filters.forEach(x=>x.classList.remove('active'));btn.classList.add('active');const f=btn.dataset.filter;const filtered=f==='all'?normalizedProjects:normalizedProjects.filter(p=>p.category===f);renderProjects(filtered,projectList);const count=document.getElementById('project-count');if(count)count.textContent=`${filtered.length} project${filtered.length===1?'':'s'}`;}));const count=document.getElementById('project-count');if(count)count.textContent=`${normalizedProjects.length} projects`;bindQuoteForm()}
async function bindQuoteForm() {
    const form = document.getElementById('quote-form');
    if (!form) return;

    const status = document.getElementById('form-status');
    const button = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        if (button) button.disabled = true;

        if (status) {
            status.className = 'form-status pending';
            status.textContent = 'Sending your request…';
        }

        const formData = new FormData(form);
        const payload = Object.fromEntries(formData.entries());

        // Ensure both full_name and name exist in payload
        payload.full_name = payload.full_name || payload.name || '';
        payload.name = payload.name || payload.full_name || '';

        // Basic client-side validation
        const requiredFields = ['full_name', 'email', 'message'];

        for (const field of requiredFields) {
            if (!String(payload[field] || '').trim()) {
                if (status) {
                    status.className = 'form-status error';
                    status.textContent = `Please provide your ${field.replace('_', ' ')}.`;
                }
                if (button) button.disabled = false;
                return;
            }
        }

        // Email validation
        const email = String(payload.email).trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {
            if (status) {
                status.className = 'form-status error';
                status.textContent = 'Please enter a valid email address.';
            }
            if (button) button.disabled = false;
            return;
        }

        try {
            console.log('Sending request to:', `${API_BASE}/quotes/`);
            const response = await fetch(`${API_BASE}/quotes/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                credentials: 'same-origin',
                body: JSON.stringify(payload)
            });

            let result = {};
            try {
                result = await response.json();
            } catch {
                result = {};
            }

            if (!response.ok) {
                let errorMessage = 'The server could not process your request.';

                if (typeof result === 'string') {
                    errorMessage = result;
                } else if (result && typeof result.detail === 'string') {
                    errorMessage = result.detail;
                } else if (result && typeof result.error === 'string') {
                    errorMessage = result.error;
                } else if (result && typeof result === 'object') {
                    // Extract field-level errors safely without [object Object]
                    const parsedErrors = [];

                    for (const [key, value] of Object.entries(result)) {
                        const fieldName = key.replace('_', ' ');
                        if (Array.isArray(value)) {
                            const messages = value.map(val => (typeof val === 'object' ? JSON.stringify(val) : String(val)));
                            parsedErrors.push(`${fieldName}: ${messages.join(', ')}`);
                        } else if (typeof value === 'string') {
                            parsedErrors.push(`${fieldName}: ${value}`);
                        } else if (typeof value === 'object' && value !== null) {
                            parsedErrors.push(`${fieldName}: ${JSON.stringify(value)}`);
                        }
                    }

                    if (parsedErrors.length > 0) {
                        errorMessage = parsedErrors.join(' | ');
                    }
                }

                // Strictly force string conversion
                throw new Error(String(errorMessage));
            }

            form.reset();

            if (status) {
                status.className = 'form-status success';
                status.textContent =
                    (typeof result.message === 'string' ? result.message : null) ||
                    'Thank you. Your request has been sent successfully. We will contact you shortly.';
            }

        } catch (error) {
            console.error('Quote submission error:', error);

            if (status) {
                status.className = 'form-status error';

                // Safely extract the string representation of error
                let displayError = 'We could not submit your request right now. Please call +234 812 684 3284 or email issabubngltd@outlook.com.';

                if (error && typeof error.message === 'string' && error.message !== '[object Object]') {
                    displayError = error.message;
                }

                status.textContent = displayError;
            }

        } finally {
            if (button) button.disabled = false;
        }
    });
}
boot();
