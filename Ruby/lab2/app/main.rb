#!/usr/bin/env ruby
# frozen_string_literal: true
require_relative 'calculate'
require_relative 'input'

if $PROGRAM_NAME == __FILE__
  obj = Input.new
  math = Calculate.new
  cnt = 1
  reg_str = '([{c,f,k}]->[(c,f,k)])$'
  reg_digit = '^[-]?[0-9]*[.]?[0-9]+$'
  while cnt == 1
    puts "Enter temperature(for float template x.xx), from->to\n"
    puts 'Temperature:'
    obj.temperature = gets.chomp.to_f
    puts 'From to example(c->f):'
    obj.from_to = gets.chomp
    if !obj.temperature.to_s.match(reg_digit) || !obj.from_to.match(reg_str)
      puts 'Incorrect input'
      next
    end
    case obj.from_to
    when 'c->f'
      puts '|c| -> |f|'
      result = math.send(:c_to_f, obj.temperature)
    when 'c->k'
      puts '|c| -> |k|'
      result = math.send(:c_to_k, obj.temperature)
    when 'f->c'
      puts '|f| -> |c|'
      result = math.send(:f_to_c, obj.temperature)
    when 'f->k'
      puts '|f| -> |k|'
      result = math.send(:f_to_k, obj.temperature)
    when 'k->f'
      puts '|k| -> |f|'
      result = math.send(:k_to_f, obj.temperature)
    when 'k->c'
      puts '|k| -> |c|'
      result = math.send(:k_to_c, obj.temperature)
    else
      puts 'Incorrect input'
      next
    end
    puts result
    puts 'To go enter 1 to exit enter another any key...'
    cnt = gets.chomp.to_i
    next if cnt == 1

    puts 'Got bye...'
    break
  end
end
