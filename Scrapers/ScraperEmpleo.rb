require_relative 'Scraper'
require_relative '../Clases/EmpleoOffer' 

class ScraperEmpleo < Scraper
    def eliminar_tildes(cadena)
      sin_tildes = super(cadena)
      sin_tildes.strip
    end
    def extraer(urlPage, archivoCsv)
      $hashOffers= {}
      begin
        puts "Scraping página: #{urlPage}"
        htmlRespuesta = HTTParty.get(urlPage, headers: HEADERS)
        puts "code : #{htmlRespuesta.code}"
        if htmlRespuesta.code == 200
          parsed_content = Nokogiri::HTML(htmlRespuesta)
          parsed_content.css(".result-item").each do |tarjetaTrabajo|
              name = tarjetaTrabajo.css("h2 a").first.inner_text
              name= eliminar_tildes(name)
              ubicacion = tarjetaTrabajo.css(".info-city").inner_text
              ubicacion = eliminar_tildes(ubicacion)
              urlhref =  tarjetaTrabajo.css("h2 a").first['href']
              puts urlhref
              salario = tarjetaTrabajo.css("li .info-salary").inner_text
              salario = eliminar_tildes(salario)
              offer = EmpleoOffer.new(name,ubicacion,urlhref, salario)
              $hashOffers[offer]=urlhref
          end
        end
        sleep(2.8)
        puts "terminando scrap de la pagina #{urlPage}..."
      rescue OpenURI::HTTPError => e
        puts "Error al acceder a la página: #{e.message}"
      rescue SocketError => e
        puts "Error de conexión: #{e.message}"

      end
      puts "Comenzando hash.."
      $hashOffers.each do |offer, href|
        puts "clave: #{offer.nombre} , ubicacion: #{offer.ubicacion} salario: #{offer.salario}=> #{href}"
        begin
          url= "https://www.elempleo.com#{href}"
          puts url
          response = HTTParty.get(url)
          puts response.code
          parsed_content = Nokogiri::HTML(response.body)
          habilidades = parsed_content.css(".ee-related-words .requirements-content span").inner_text
          formacion= parsed_content.css(".offer-data-additional .js-education-level").inner_text
          divs = parsed_content.css('.offer-data-additional .col-xs-12.col-sm-6.data-column')
          segundo_div = divs[1]
          experiencia = segundo_div.css('span').text.strip
          descripcion = 
          begin
              parsed_content.css('.description-block p').text.strip
          rescue StandardError
          "Descripción no disponible"
          end
          habilidades= eliminar_tildes(habilidades)
          formacion= eliminar_tildes(formacion)
          experiencia= eliminar_tildes(experiencia)
          descripcion = eliminar_tildes(descripcion)
          offer.setHabilidades(habilidades)
          offer.setFormacion(formacion)
          offer.setExperiencia(experiencia)
          offer.setDescripcion(descripcion)

          begin
            offer.save(archivoCsv)
            puts "Guardado correctamente: #{offer.nombre}"
          rescue StandardError => e
            puts "Error al guardar en el CSV: #{e.message}"
          end
          sleep(1.4)
          rescue StandardError => e
          puts "Error al acceder a #{url}: #{e.message}"
        end
      end
    end
end
