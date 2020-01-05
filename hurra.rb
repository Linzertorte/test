#! /usr/bin/ruby
require 'nokogiri'
require 'open-uri'
require 'colorize'

def clean_print(t,ind)
  t.each_line do |line|
    line.strip!
    puts (" "*ind).concat line if line!=""
  end
end

def print_example(pair,ind)
  puts (" "*ind).concat pair.css('.eg').text.green.bold  # green
  clean_print(pair.css('.hdb').text,ind)
  puts
end

def print_sense(body)
  body.css('> div.def-block').each do |blk|
    print_def(blk,0) if !blk.classes.include?('ddef_block-nos')
  end
  body.css('.phrase-block').each do |blk|
    print_phrase(blk)
  end
end

def print_def(defi,ind)
  puts (" "*ind).concat defi.css('.def-head').text if defi.css('.def-head').text !=""
  puts (" "*ind).concat defi.css('.def-body').css('> span.trans').text.red #read
  puts
  defi.css('.def-body').css('.examp').each do |pair|
    print_example(pair,ind + 2)
  end
end

def print_phrase(blk)
  puts blk.css('.phrase-head').text.gsub(/^[[:space:]]+/, '').light_blue
  blk.css('.def-block').each do |d|
    print_def(d, 2)
  end
end

def print_di(di)
  puts "----".cyan.bold
  head = di.css('.di-head')
  body = di.css('.di-body')

  puts head.css('.di-title').text
  puts head.css('.di-info').text
  puts

  body.css('.sense-body').each do |blk|
    print_sense(blk)
  end
end

word = ARGV[0].dup
word.gsub! 'ą','a'
word.gsub! 'ć','c'
word.gsub! 'ę','e'
word.gsub! 'ł','l'
word.gsub! 'ń','n'
word.gsub! 'ś','s'
word.gsub! 'ź','z'
word.gsub! 'ż','z'
word.gsub! 'ó','o'


u = 'https://dictionary.cambridge.org/us/dictionary/polish-english/'.concat(word)
doc = Nokogiri::HTML(open(u))

puts `clear`

entry = doc.css('.dictionary')[0]
entry.css('.di').each do |di|
  print_di(di)
end
