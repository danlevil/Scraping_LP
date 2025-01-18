require_relative 'Scraper'
require_relative '../Clases/BuscoJobsOffer' 

class ScraperBuscoJobs < Scraper

    def extraer(urlPage, archivoCsv)
        $hashOffers= {}
        (1..16).each do |page|
        begin
            url= "#{urlPage}/#{page}"
            puts "Scraping página: #{url}"
            htmlRespuesta = HTTParty.get(url, headers: HEADERS)
            puts "code : #{htmlRespuesta.code}"
            if htmlRespuesta.code == 200
                parsed_content = Nokogiri::HTML(htmlRespuesta)
                parsed_content.css(".ListadoOfertas_result__vlmRK").each do |tarjetaTrabajo|
                    name = tarjetaTrabajo.css(".ListadoOfertas_oferta__6GIri h3 a").inner_text
                    name= eliminar_tildes(name)
                    urlhref =  tarjetaTrabajo.css("a").first['href']
                    ubicacion = "None"
                    offer = BuscoJobsOffer.new(name,ubicacion,urlhref)
                    $hashOffers[offer]=urlhref
                    puts "Guardando datos en el Hash"
                end
            end
            sleep(2.8)
            puts "terminando scrap de la pagina #{page}..."

        rescue OpenURI::HTTPError => e
            puts "Error al acceder a la página: #{e.message}"
        rescue SocketError => e
            puts "Error de conexión: #{e.message}"
        end
    end

    puts "Comenzando hash.."
    $hashOffers.each do |offer, href|
        begin
            url = "https://www.buscojobs.com.ec#{href}"
            response = HTTParty.get(url, headers: HEADERS)
            parsed_content = Nokogiri::HTML(response.body)

            descripcion = 
            begin
                parsed_content.css('.OfertaDetalle_descripcion_texto__DCV1g p').text.strip
            rescue StandardError
            "Descripción no disponible"
            end
            descripcion = eliminar_tildes(descripcion)
            offer.setDescripcion(descripcion)
            begin
                offer.save(archivoCsv)
                puts "Guardado correctamente: #{offer.nombre}"
            rescue StandardError => e
                puts "Error al guardar en el CSV: #{e.message}"
            end
            sleep(1)
        rescue StandardError => e
            puts "Error al acceder a #{url}: #{e.message}"
        end
    end
    end
end