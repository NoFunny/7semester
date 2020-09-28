#!/usr/bin/env ruby
# frozen_string_literal: true

# Description/Explanation of Calculate class
class Calculate

  def c_to_f(temp)
    ((temp * 1.8) + 32).round(2)
  end

  def c_to_k(temp)
    (temp + 273.15).round(2)
  end

  def f_to_k(temp)
    ((temp - 32) / 1.8 + 273.15).round(2)
  end

  def f_to_c(temp)
    ((temp - 32) / 1.8).round(2)
  end

  def k_to_f(temp)
    ((temp - 273.15) * 1.8 + 32).round(2)
  end

  def k_to_c(temp)
    (temp - 273.15).round(2)
  end
end
