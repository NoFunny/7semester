# frozen_string_literal: true

require '../app/lab3.rb'
require 'csv'

describe ReadCSV do
  describe '.get_header' do
    context 'Incorrect value in header' do
      let(:read) { ReadCSV.new }
      it 'Incorrect value in header' do
        expect(read.get_header('../resources/testData1.csv')).to eq nil
      end
    end
  end
end

describe ReadCSV do
  describe '.get_years' do
    context 'Incorrect value in years' do
      let(:read) { ReadCSV.new }
      it 'Incorrect value in array for extracting years' do
        csv = read.get_csv('../resources/testData2.csv')
        headers = read.get_header('../resources/testData2.csv')
        expect(read.get_years(csv, headers[0])).to eq nil
      end
    end
  end
end

describe ReadCSV do
  describe '.get_countries' do
    context 'Incorrect value in countries' do
      let(:read) { ReadCSV.new }
      it 'Incorrect value in array for extracting countries' do
        csv = read.get_csv('../resources/testData2.csv')
        headers = read.get_header('../resources/testData2.csv')
        expect(read.get_countries(csv, headers[1])).to eq nil
      end
    end
  end
end

describe ReadCSV do
  describe '.get_summary' do
    context 'Incorrect value in summary' do
      let(:read) { ReadCSV.new }
      it 'Incorrect value in array for extracting summary' do
        csv = read.get_csv('../resources/testData2.csv')
        headers = read.get_header('../resources/testData2.csv')
        expect(read.get_summary(csv, headers[2])).to eq nil
      end
    end
  end
end

describe ReadCSV do
  describe '.get_header' do
    context 'Correct value in header' do
      let(:read) { ReadCSV.new }
      it 'Correct value in header' do
        expect(read.get_header('../resources/data.csv')).to eq %w[Год Страны Всего]
      end
    end
  end
end

describe ReadCSV do
  describe '.get_years' do
    context 'Correct value in years' do
      let(:read) { ReadCSV.new }
      it 'Correct value in array for extracting years' do
        csv = read.get_csv('../resources/testData3.csv')
        csv_anyway_correct = read.get_csv('../resources/data.csv')
        headers = read.get_header('../resources/data.csv')
        years_anyway_correct = read.get_years(csv_anyway_correct, headers[0])
        expect(read.get_years(csv, headers[0])).to eq years_anyway_correct
      end
    end
  end
end

describe ReadCSV do
  describe '.get_countries' do
    context 'Correct value in countries' do
      let(:read) { ReadCSV.new }
      it 'Correct value in array for extracting countries' do
        csv = read.get_csv('../resources/testData3.csv')
        csv_anyway_correct = read.get_csv('../resources/data.csv')
        headers = read.get_header('../resources/data.csv')
        countries_anyway_correct = read.get_countries(csv_anyway_correct, headers[1])
        expect(read.get_countries(csv, headers[1])).to eq countries_anyway_correct
      end
    end
  end
end

describe ReadCSV do
  describe '.get_summary' do
    context 'Correct value in summary' do
      let(:read) { ReadCSV.new }
      it 'Correct value in array for extracting summary' do
        csv = read.get_csv('../resources/testData3.csv')
        csv_anyway_correct = read.get_csv('../resources/data.csv')
        headers = read.get_header('../resources/data.csv')
        summary_anyway_correct = read.get_summary(csv_anyway_correct, headers[2])
        expect(read.get_summary(csv, headers[2])).to eq summary_anyway_correct
      end
    end
  end
end

describe Calculate do
  describe '.min' do
    context 'Correct value in array, checked result min' do
      let(:calc) { Calculate.new }
      it 'Check result min' do
        test_data = [123, 234, 456, 678, 234_234, 123_123, 657_567, 8768, 111_111_111]
        expect(calc.min(test_data)).to eq 123
      end
    end
  end
end

describe Calculate do
  describe '.max' do
    context 'Correct value in array, checked result max' do
      let(:calc) { Calculate.new }
      it 'Check result max' do
        test_data = [123, 234, 456, 678, 234_234, 123_123, 657_567, 8768, 111_111_111]
        expect(calc.max(test_data)).to eq 111_111_111
      end
    end
  end
end

describe Calculate do
  describe '.avg' do
    context 'Correct value in array, checked result avg' do
      let(:calc) { Calculate.new }
      it 'Check result avg' do
        test_data = [123, 234, 456, 678, 234_234, 123_123, 657_567, 8768, 111_111_111]
        expect(calc.avg(test_data)).to eq 12_459_588.22
      end
    end
  end
end

describe Calculate do
  describe '.correct_sample_variance' do
    context 'Correct value in array, checked result correct sample variance' do
      let(:calc) { Calculate.new }
      it 'Check result correct sample variance' do
        test_data = [123, 234, 456, 678, 234_234, 123_123, 657_567, 8768, 111]
        expect(calc.correct_sample_variance(test_data)).to eq 48_211_717_455.28
      end
    end
  end
end
