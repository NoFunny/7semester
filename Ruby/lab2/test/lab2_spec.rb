# frozen_string_literal: true

require '../app/lab2.rb'

describe Calculate do
  describe '.calc' do
    context 'Calc method.' do
      let(:obj) { Calculate.new }
      it 'Return nil(Float temp)' do
        expect(obj.calc(23.432, 'c', 'q')).to eq nil
      end
      it 'Return nil(Incorrect temp)' do
        expect(obj.calc('123,234', '', '')).to eq nil
      end
      it 'Return nil(Incorrect to)' do
        expect(obj.calc(2, 'c', 't')).to eq nil
      end
      it 'Return nil(Incorrect from)' do
        expect(obj.calc(15, 'd', 'f')).to eq nil
      end
      it 'Return nil(Empty temp)' do
        expect(obj.calc(0.0, 'c', 'f')).to eq nil
      end
      it 'Return nil(Empty from)' do
        expect(obj.calc(123.234, '', 'c')).to eq nil
      end
      it 'Return nil(Empty to)' do
        expect(obj.calc(123.234, 'c', '')).to eq nil
      end
      it 'Return nil(Empty from, to)' do
        expect(obj.calc(123.234, '', '')).to eq nil
      end
      it 'Return nil(C -> F)' do
        expect(obj.calc(32, 'c', 'f')).to eq 89.60
      end
      it 'Return nil(C -> K)' do
        expect(obj.calc(32, 'c', 'k')).to eq 305.15
      end
      it 'Return nil(K -> C)' do
        result = obj.calc(32, 'k', 'c')
        expect(result.round(2)).to eq -241.15
      end
      it 'Return nil(K -> F)' do
        result = obj.calc(32, 'k', 'f')
        expect(result.round(2)).to eq -402.07
      end
      it 'Return nil(F -> C)' do
        expect(obj.calc(32, 'f', 'c')).to eq 0.00
      end
      it 'Return nil(F -> K)' do
        expect(obj.calc(32, 'f', 'k')).to eq 273.15
      end
    end
  end
end

