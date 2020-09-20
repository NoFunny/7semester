#!/usr/bin/env ruby
# frozen_string_literal: true

require 'csv'

# Description/Explanation of ReadCSV class
class ReadCSV
  def get_header(file_name)
    reg_string = '^([а-яА-Я]{0,}?[a-zA-Z]{0,}?\s{0,}?[а-яА-Я]{0,}?[a-zA-Z]{0,})$'
    CSV.read(file_name)[0].each do |el|
      return nil unless el.match(reg_string)
    end
    CSV.read(file_name)[0]
  end

  def get_csv(file_name)
    CSV.read(file_name, headers: true)
  end

  def get_years(csv, names)
    reg_date = '^[0-9]{4}$'
    csv[names].each do |el|
      return nil unless el.match(reg_date)
    end
    csv[names]
  end

  def get_countries(csv, names)
    reg_string = '^([а-яА-Я]{0,}?[a-zA-Z]{0,}?\s{0,}?[а-яА-Я]{0,}?[a-zA-Z]{0,})$'
    csv[names].each do |el|
      return nil unless el.match(reg_string)
    end
    csv[names]
  end

  def get_summary(csv, names)
    reg_digit = '^[-]?[0-9]*[.]?[0-9]+$'
    csv[names].each do |el|
      return nil unless el.match(reg_digit)
    end
    csv[names].map(&:to_i)
  end
end

# Description/Explanation of Calculate class
class Calculate
  def min(array)
    array.min
  end

  def max(array)
    array.max
  end

  def avg(array)
    (array.inject { |sum, el| sum + el }.to_f / array.size).round(2)
  end

  def correct_sample_variance(array)
    avg = self.avg(array)
    iter = array.map { |el| (el - avg)**2 }
    iter = iter.inject(:+)
    iter /= array.length - 1
    iter.round(2)
  end
end

if $PROGRAM_NAME == __FILE__
  read = ReadCSV.new
  names = read.get_header('/home/nofunny/Study/Ruby/lab3/resources/data.csv')
  csv = read.get_csv('/home/nofunny/Study/Ruby/lab3/resources/data.csv')
  if names.nil?
    puts 'Incorrect csv'
    return
  end

  years = read.get_years(csv, names[0])
  p countries = read.get_countries(csv, names[1])
  summary = read.get_summary(csv, names[2])
  if years.nil? || countries.nil? || summary.nil?
    puts 'Incorrect csv'
    return
  end

  calc = Calculate.new
  p summary.class
  p 'Min value'
  p calc.min(summary)
  p 'Max value'
  p calc.max(summary)
  p 'Average value'
  p calc.avg(summary)
  p 'Correct sample variance'
  p calc.correct_sample_variance(summary)
end
