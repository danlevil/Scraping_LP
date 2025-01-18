require_relative 'JobOffer'
require 'csv'
class BuscoJobsOffer < JobOffer

  def initialize(nombre, ubicacion, url, salario ="None" , modalidad = "None", descripcion = "None")
    super(nombre, ubicacion, url, salario, modalidad,  descripcion)
  end

  def save (filecsv)    
    CSV.open(filecsv, 'a') do |csv|
      csv << [@nombre, @ubicacion, @url, @salario, @modalidad, @descripcion]
    end
  end
  def hash
    @nombre.hash
  end
end
