# frozen_string_literal: true

require '../app/lab2.rb'


describe Calculate do
  describe '.c_to_f' do
    context 'c_to_f method check on correct value.' do
      let(:obj) { Calculate.new }
      it '32' do
        expect(obj.c_to_f(32)).to eq 89.6
      end
      it '34.5' do
        expect(obj.c_to_f(34.5)).to eq 94.1
      end
      it '-35' do
        expect(obj.c_to_f(-35)).to eq(-31)
      end
    end
  end
end

describe Calculate do
  describe '.c_to_k' do
    context 'c_to_k method check on correct value.' do
      let(:obj) { Calculate.new }
      it '32' do
        expect(obj.c_to_k(32)).to eq 305.15
      end
      it '34.5' do
        expect(obj.c_to_k(34.5)).to eq 307.65
      end
      it '-35' do
        expect(obj.c_to_k(-35)).to eq 238.15
      end
    end
  end
end

describe Calculate do
  describe '.f_to_c' do
    context 'f_to_c method check on correct value.' do
      let(:obj) { Calculate.new }
      it '76' do
        expect(obj.f_to_c(76)).to eq 24.44
      end
      it '89.67' do
        expect(obj.f_to_c(89.67)).to eq 32.04
      end
      it '-35' do
        expect(obj.f_to_c(-35)).to eq(-37.22)
      end
    end
  end
end

describe Calculate do
  describe '.f_to_k' do
    context 'f_to_k method check on correct value.' do
      let(:obj) { Calculate.new }
      it '76' do
        expect(obj.f_to_k(76)).to eq 297.59
      end
      it '89.67' do
        expect(obj.f_to_k(89.67)).to eq 305.19
      end
      it '-35' do
        expect(obj.f_to_k(-35)).to eq 235.93
      end
    end
  end
end

describe Calculate do
  describe '.k_to_c' do
    context 'k_to_c method check on correct value.' do
      let(:obj) { Calculate.new }
      it '356' do
        expect(obj.k_to_c(356)).to eq 82.85
      end
      it '300.56' do
        expect(obj.k_to_c(300.56)).to eq 27.41
      end
      it '-35' do
        expect(obj.k_to_c(-35)).to eq(-308.15)
      end
    end
  end
end

describe Calculate do
  describe '.k_to_f' do
    context 'k_to_f method check on correct value.' do
      let(:obj) { Calculate.new }
      it '356' do
        expect(obj.k_to_f(356)).to eq 181.13
      end
      it '300.56' do
        expect(obj.k_to_f(300.56)).to eq 81.34
      end
      it '-35' do
        expect(obj.k_to_f(-35)).to eq(-522.67)
      end
    end
  end
end
