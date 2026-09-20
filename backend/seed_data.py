import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
import django
django.setup()
from company.models import CompanyProfile
from services.models import Service
from projects.models import Project
CompanyProfile.objects.update_or_create(id=1,defaults={
'name':'ISSABUB Nigeria Limited','tagline':'Your vision, our execution.',
'description':'Issabub Nigeria Limited is an Ogun-based general construction and civil engineering firm providing comprehensive project execution for residential, commercial, industrial, and infrastructure clients across Nigeria. Founded on January 28, 2014, with operations from the Ijoko Ota corridor.',
'mission':'To deliver high-quality building and civil engineering projects that meet exact standards—delivered on time, within budget, and with uncompromising structural integrity and site safety.',
'vision':'To remain a dependable, first-choice general contracting firm across Ogun State and Nigeria, recognized for technical capability in both structural building and vital infrastructure development.',
'address':'15, Kajola Estate, Ifelodun Street, Off Gasline, Ijoko Ota, Ogun State','phone':'+2348126843284','email':'issabubngltd@outlook.com',
'business_hours':{'monday':'8:00 AM – 6:00 PM','tuesday':'8:00 AM – 6:00 PM','wednesday':'8:00 AM – 6:00 PM','thursday':'8:00 AM – 6:00 PM','friday':'8:00 AM – 6:00 PM','saturday':'8:00 AM – 3:00 PM','sunday':'Closed'},
'statistics':{'years_active':'12+','projects_completed':'120+','happy_clients':'80+','safety_rating':'0.92'}})
services=[
('01','Technical Sub-Contracting','technical-sub-contracting','Specialized labor, skilled manpower, and execution support for large-scale industrial and EPC projects.',['Access to skilled technical personnel','Rapid mobilization and flexible workforce scaling','Industrial and EPC execution support','Safety, quality and schedule discipline'],'Industrial plants, EPC project execution and site works, oil & gas, power, mining, manufacturing, shutdowns and structural erection.','assets/images/service-technical.jpg'),
('02','Mechanical Engineering','mechanical-engineering','Design, analysis and engineering support for mechanical systems and equipment, including fabrication, installation and commissioning.',['Expert design and engineering analysis','Mechanical systems and equipment support','Fabrication and precision manufacturing','Technical support and optimization'],'Industrial machinery, production equipment, piping, HVAC, process equipment and EPC mechanical installations.','assets/images/service-mechanical.jpg'),
('03','Industrial Maintenance','industrial-maintenance','Scheduled and emergency maintenance services for industrial facilities, machinery and critical systems to reduce downtime and extend asset life.',['Preventive maintenance programs','Emergency repair and breakdown support','Experienced industrial technicians','Maintenance reporting and compliance'],'Manufacturing plants, machinery, shutdowns, turnarounds, pumps, conveyors, boilers and process equipment.','assets/images/service-maintenance.jpg'),
('04','Building & Construction','building-construction','Complete building construction from groundwork and foundations through structural works, finishing and handover.',['End-to-end project management','Site engineering supervision','Quality and timeline control','Safety and regulatory compliance'],'Residential homes, estates, apartments, offices, shops, warehouses, factories, schools, hospitals, extensions and refurbishments.','assets/images/service-construction.jpg')]
for n,t,s,d,b,a,img in services: Service.objects.update_or_create(slug=s,defaults={'number':n,'title':t,'description':d,'key_benefits':b,'applications':a,'image':img,'active':True})
projects=[
('Retail Shopping Centre Expansion','commercial','Expansion of an existing shopping centre adding 2,800 sqm of new retail and food-court space. The scope includes structural works, external envelope, public plazas and integration with existing systems.','assets/images/project-retail.jpg'),
('Office Building Shell & Core','commercial','Construction of a four-storey commercial office building of approximately 3,200 sqm, including structural frame, façade, core services and base-build systems.','assets/images/project-office-shell.jpg'),
('Commercial Warehouse Frame','commercial','Full structural steel framework for a 1,200 sqm warehouse including columns, beams, purlins, wall girts, bracing, base plates and connections.','assets/images/project-warehouse.jpg'),
('Apartment Fit-Out & Interiors','residential','Complete interior fit-out of a 12-unit residential apartment block including kitchens, bathrooms, flooring, joinery, ceilings, lighting, plumbing and electrical works.','assets/images/project-apartment.jpg'),
('Townhouse Development','residential','Turnkey construction of an eight-unit contemporary townhouse development with private courtyards, parking, modern interiors and shared landscaped areas.','assets/images/project-townhouse.jpg'),
('Family Home Extension & Remodel','residential','Major rear extension and internal remodel involving structural modifications, new living areas, upgraded bathrooms and integrated finishes.','assets/images/project-family.jpg'),
('Clinker Transport System Repair','retrofitting','Comprehensive repair and rehabilitation of a clinker transport system including structural assessment, frame strengthening, steel replacement, conveyor support repair and safety systems.','assets/images/project-clinker.jpg'),
('Industrial Facility Upgrade','retrofitting','Retrofitting of an existing industrial building including structural strengthening, roof replacement, cladding upgrades, insulation and mechanical/electrical modernisation.','assets/images/project-industrial-upgrade.jpg'),
('Office Space Refurbishment','retrofitting','Complete interior renovation of a commercial office floor with partitions, suspended ceilings, raised flooring, lighting, HVAC, electrical and data installations.','assets/images/project-office-refurbishment.jpg'),
('Sports Arena Roof Truss','structural','Long-span steel space-frame roof structure spanning 80 metres for an indoor multi-purpose arena, including trusses, purlins, bracing and access walkways.','assets/images/project-arena.jpg'),
('Industrial Portal Frame Building','structural','Design, fabrication and erection of a large-span steel portal frame for a manufacturing facility supporting crane runway beams, heavy equipment loads and access platforms.','assets/images/project-portal.jpg'),
('Integration of Existing Cement Silo','structural','Integration of an existing cement silo with a new process line through steelwork, platforms, access structures and connections.','assets/images/project-silo.jpg')]
for title,cat,d,img in projects:
    slug=title.lower().replace('&','and').replace(' ','-')
    Project.objects.update_or_create(slug=slug,defaults={'title':title,'category':cat,'description':d,'image':img,'featured':title in {'Retail Shopping Centre Expansion','Commercial Warehouse Frame','Integration of Existing Cement Silo'}})
print('Seed complete')
