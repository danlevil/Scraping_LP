
class Scraper
  require 'open-uri'
  require 'nokogiri'
  require 'csv'
  require 'fileutils'
  require 'httparty'
  HEADERS = {
    "User-Agent" => "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  }
  def eliminar_tildes(cadena)
    sinTildes=cadena.tr(
        'áéíóúÁÉÍÓÚñÑüÜ',
        'aeiouAEIOUnNuU'
    )
    caracteres_a_eliminar = /[!¡¿?]/
    sinTildes.gsub(caracteres_a_eliminar, '')
  end
end
