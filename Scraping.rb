require 'open-uri'
require 'nokogiri'
require 'csv'
require 'fileutils'
require 'httparty'
require_relative 'Clases/BuscoJobsOffer'
require_relative 'Clases/JobOffer'
require_relative 'Scrapers/ScraperBuscoJobs'
require_relative  'Scrapers/ScraperEmpleo'
require_relative  'Scrapers/ScraperCompuTrabajos'
require_relative  'Scrapers/ScraperInfoJobs'


PATH_BuscoJobsCSV     = "datosCSV/BuscoJobs_ofertas.csv"
PATH_ComputrabajoCSV  = "datosCSV/CompuTrabajo_ofertas.csv"
PATH_InfoJobsCSV      = "datosCSV/InfoJobs_ofertas.csv" #España
PATH_EmpleosCSV      = "datosCSV/Empleo_ofertas.csv"  #Colombia

Dir.mkdir("datosCSV") unless Dir.exist?("datosCSV")
csv_files = {
    PATH_BuscoJobsCSV => [ "Nombre" , "Ubicacion", "Url", "Salario", "Modalidad", "Descripcion"],
    PATH_ComputrabajoCSV => ["Nombre", "Ubicacion","Salario","Modalidad","Idioma", "Experiencia" ,"Conocimientos","Url",  "Descripcion"],
    PATH_InfoJobsCSV  => ["Nombre", "Ubicacion","Salario","Modalidad","Jornada","Idioma", "Experiencia" "Url",  "Descripcion"],
    PATH_EmpleosCSV  => [ "Nombre" , "Ubicacion", "Salario" , "Habilidades Clave", "Formacion", "Experiencia","Modalidad", "Url", "Descripcion"]
}
csv_files.each do |file_path, headers|
    unless File.exist?(file_path)
        CSV.open(file_path, "w") do |csv|
            csv << headers  
        end
        puts "Archivo creado: #{file_path}"
    else
        puts "El archivo ya existe: #{file_path}"
    end
end

#https://ec.computrabajo.com/trabajo-de-desarrollador?p=1
url_buscoJobs     = "https://www.buscojobs.com.ec/ofertas/ts1017/trabajo-de-tecnologia-de-la-informacion" 
url_compuTrabajo  = "https://ec.computrabajo.com/trabajo-de-desarrollador?" 
url_infoJobs      = "https://www.infojobs.net/ofertas-trabajo?keyword=Software&segmentId=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=17&sinceDate=ANY" 
url_elempleo        = "https://www.elempleo.com/co/ofertas-empleo/trabajo-desarrollador" 



#----------Scraper BuscoJobs.com--------------------
# sc = ScraperBuscoJobs.new()
# sc.extraer(url_buscoJobs, PATH_BuscoJobsCSV2)

#----------Scraper Empleo.co------------------------
# sc = ScraperEmpleo.new()
# sc.extraer(url_elempleo, PATH_EmpleosCSV)
# 

#----------Scraper CompuTrabajos.com----------------
sc = ScraperCompuTrabajos.new()
sc.extraer(url_compuTrabajo , PATH_ComputrabajoCSV)


#---------Scraper InfoJobs.com----------------------
# sc = ScraperInfoJobs.new()
# sc.extraer(PATH_InfoJobsCSV)


