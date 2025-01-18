require_relative 'Scraper'
require_relative '../Clases/CompuTrabajoOffer' 


class ScraperCompuTrabajos < Scraper
  def eliminar_tildes(cadena)
    sin_tildes = super(cadena)
    sin_tildes.strip
  end

  def extraer (urlPage, archivoCsv)
    $hashOffers= {}
    (1..5).each do |page|
      begin
        url = "#{urlPage}p=#{page}"
        puts "Scraping página: #{url}"
        htmlRespuesta = HTTParty.get(url, headers: HEADERS)
        puts "code : #{htmlRespuesta.code}"
        
        if htmlRespuesta.code == 200
          parsed_content = Nokogiri::HTML(htmlRespuesta)
          
          parsed_content.css(".box_offer").each do |tarjetaTrabajo|
              name = eliminar_tildes(tarjetaTrabajo.css("h2 a").inner_text)
              ubicacion = eliminar_tildes(tarjetaTrabajo.css("p .mr10").inner_text)
              modalidad = eliminar_tildes(tarjetaTrabajo.css("div .mr10").inner_text)
              urlhref= tarjetaTrabajo.css("h2 a").first['href']
              offer = CompuTrabajoOffer.new(name, ubicacion, urlhref)
              offer.setModalidad(modalidad)
              $hashOffers[offer]= urlhref
              #data_id = tarjetaTrabajo.at_xpath('.//@data-id').value 

            end
          end

        puts "terminando scrap de la pagina #{page}..."
      rescue OpenURI::HTTPError => e
        puts "Error al acceder a la página: #{e.message}"
      rescue SocketError => e
        puts "Error de conexión: #{e.message}"

      end
    end
    user_agents = [
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
    ]
    puts "Comenzando hash.."
    $hashOffers.each do |offer, href|
      begin
        user_agent = user_agents.sample
        headers = { 
          "User-Agent" => user_agent, 
          "Accept" => "application/json", 
          "Connection" => "close" 
        }
        url = "https://ec.computrabajo.com#{href}"
        puts url
        response = HTTParty.get(url, headers: headers)
        puts response.code
        parsed_content = Nokogiri::HTML(response.body)
        li_elements = parsed_content.css('div[div-link="oferta"] ul li')
        conocimientos = eliminar_tildes(li_elements[3].text.strip)
        experiencia = eliminar_tildes(li_elements[1].text.strip)
        idioma = eliminar_tildes(li_elements[2].text.strip)
        offer.setConocimientos(conocimientos)
        offer.setExperiencia(experiencia)
        offer.setIdioma(idioma)
        begin
          offer.save(archivoCsv)
          puts "Guardado correctamente: #{offer.nombre}"
        rescue StandardError => e
          puts "Error al guardar en el CSV: #{e.message}"
        end
        sleep(rand(3..6)) 
        rescue StandardError => e
          puts "Error al acceder a #{url}: #{e.message}"

      end
    end
  end

end