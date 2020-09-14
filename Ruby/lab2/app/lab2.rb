#!/usr/bin/env ruby
# frozen_string_literal: true

class Input
  attr_accessor :temperature, :from, :to
end

class Calculate
  attr_accessor :result

  # @param [Object] temp
  # @param [Object] from
  # @param [Object] to
  def calc(temp, from, to)
    return nil if temp == 0.0 || from.empty? || to.empty?

    if from == 'c' || from == 'k' || from == 'f' &&
                                       to == 'c' || to == 'k' || to == 'f'
      @result = temp * 1.8 + 32 if from == 'c' && to == 'f'
      @result = temp + 273.15 if from == 'c' && to == 'k'
      @result = (temp - 32) * 1.8 if from == 'f' && to == 'c'
      @result = temp - 273.15 if from == 'k' && to == 'c'
      @result = (temp - 32) * 1.8 + 273.15 if from == 'f' && to == 'k'
      @result = (temp - 273.15) * 1.8 + 32 if from == 'k' && to == 'f'
      @result
    else
      puts 'Incorrect input data, return...'
      nil
    end
  end
end

obj = Input.new
math = Calculate.new
cnt = 1
if $PROGRAM_NAME == __FILE__
  while cnt == 1
    puts "Enter temperature(for float template x.xx), from --> to\n"
    puts 'Temperature:'
    obj.temperature = gets.chomp.to_f
    puts 'From:'
    obj.from = gets.chomp
    puts 'To:'
    obj.to = gets.chomp
    puts '|c| -> |f|' if obj.from == 'c' && obj.to == 'f'
    puts '|c| -> |k|' if obj.from == 'c' && obj.to == 'k'
    puts '|f| -> |c|' if obj.from == 'f' && obj.to == 'c'
    puts '|k| -> |c|' if obj.from == 'k' && obj.to == 'c'
    puts '|f| -> |k|' if obj.from == 'f' && obj.to == 'k'
    puts '|k| -> |f|' if obj.from == 'k' && obj.to == 'f'
    result = math.calc(obj.temperature, obj.from, obj.to)
    printf("Result = %.2f\n", result.to_f) unless result.nil?
    puts 'To go enter 1 to exit enter 0...'
    cnt = gets.chomp.to_i
    if cnt.zero?
      puts 'Got bye...'
      break
    else next
    end
  end
end
