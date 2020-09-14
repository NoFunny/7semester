#!/usr/bin/env ruby

class Input
  attr_accessor :temperature
end

class Calculate
  attr_accessor :result

  def self.calc(temp, from, to)
    return if temp.zero? || from.empty? || to.empty?

    if from == 'c' || from == 'k' || from == 'f' &&
                                     to == 'c' || to == 'k' || to == 'f'
      @result = temp * 1.8 + 32 if from == 'c' && to == 'f'
      @result = temp + 273 if from == 'c' && to == 'k'
      @result = (temp - 32) / 1.8 if from == 'f' && to == 'c'
      @result = temp - 273 if from == 'k' && to == 'c'
      @result = (temp - 32) * 0.55555555555 + 273 if from == 'f' && to == 'k'
      @result = (temp - 32) * 0.55555555555 + 32 if from == 'k' && to == 'f'
      @result
    else
      puts 'Incorrect input data, return...'
      return 100500
    end
  end
end

obj = Input.new
cnt = 1
if $PROGRAM_NAME == __FILE__
  while cnt == 1
    puts "Enter temperature, from --> to\n"
    puts 'Temperature:'
    obj.temperature = gets.chomp.to_f
    puts 'From:'
    from = gets.chomp
    puts 'To:'
    to = gets.chomp
    puts '|c| -> |f|' if from == 'c' && to == 'f'
    puts '|c| -> |k|' if from == 'c' && to == 'k'
    puts '|f| -> |c|' if from == 'f' && to == 'c'
    puts '|k| -> |c|' if from == 'k' && to == 'c'
    puts '|f| -> |k|' if from == 'f' && to == 'k'
    puts '|k| -> |f|' if from == 'k' && to == 'f'
    result = Calculate.calc(obj.temperature, from, to)
    printf("Result = %3f\n", result.to_f) if result != 100500
    puts 'To go enter 1 to exit enter 0...'
    cnt = gets.chomp.to_i
    if cnt.zero?
      puts 'Got bye...'
      break
    else next
    end
  end
end

