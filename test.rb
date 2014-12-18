#!/usr/bin/env ruby

require 'unlimited-jce-policy-jdk7'

['AES', 'DH'].each do |cipher|
  puts "Maximum allowed key length for #{cipher}: #{javax.crypto::Cipher.getMaxAllowedKeyLength(cipher)}"
end
