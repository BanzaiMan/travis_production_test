source 'http://rubygems.org'

gem 'rails',              '~> 4.1.14.0'
gem 'mysql2',             '~> 0.3.16'
gem 'kaminari',           '~> 0.16.1'
gem 'wristband',          '~> 2.3.2'
gem 'konf',               '~> 0.0.2'
gem 'postageapp',         '~> 1.0.23'
gem 'airbrake',           '~> 4.0.0'
gem 'faker',              '~> 1.4.3'
gem 'dirigible',          git: 'https://github.com/z5h/dirigible.git', branch: 'development'
gem 'rest-client',        '~> 1.7.2'
gem 'nokogiri',           '~> 1.6.3.1'
gem 'activerecord-import','~> 0.5.0'
gem 'demoji'
gem 'dalli'
gem 'active_type',        '~> 0.3.1'
gem 'obscenity'

# used in tests but also in seed scripts to play out events over time
gem 'timecop',            '~> 0.7.1'

#sidekiq stuff
gem 'sidekiq',            '~> 3.3'
gem 'capistrano-sidekiq', '0.3.4' #bug in 0.3.5
gem 'unicorn',            '~> 4.8.3'
# if you require 'sinatra' you get the DSL extended to Object
gem 'sinatra', '>= 1.3.0', :require => nil

# monitoring
gem 'newrelic_rpm',       '~> 3.9.3.241'

# Front end stuff
gem 'haml',               '~> 4.0.5'
gem 'jquery-rails',       '~> 2.1.3'
gem 'active_link_to',     '~> 1.0.2'
gem 'rails-backbone',     '~> 0.9.10'
gem 'eco',                '~> 1.0.0'
gem 'bootstrap_builder',  '~> 0.4.0'
gem 'jbuilder',           '~> 2.1.3'

gem 'react-rails', '~> 0.12.0'

# new twitter bootstrap stuff
# will use only in new reoports, and migrate things over as time allows
gem 'bootstrap-sass', '~> 3.2.0'
gem 'autoprefixer-rails'

# Rails 4 moves assets stuff to top level
gem 'sass-rails',               '~> 5.0.0'
gem 'coffee-rails',             '~> 4.0.1'
gem 'coffee-rails-source-maps', '~> 1.4.0'
gem 'uglifier',                 '~> 2.5.3'

# rails 4 compatibily stuff. remove as they become
# unnecessary through refactorings

gem 'actionview-encoded_mail_to', '~>1.0.4'

group :test do
  gem 'simplecov', :require => false
  gem 'test_after_commit','~> 0.2.5'

  gem 'webmock' #NEVER hit the web from a test unless we've explicitely VCR recorded it
  gem 'vcr'     #records web requests so we can play them back for reliable testing
end

group :development, :profile do
  gem 'license_finder',     :require => false
  gem 'thin',               '~> 1.6.2'
  gem 'pry',                '~> 0.10.1'
  gem 'byebug'
  gem 'pry-byebug'

  gem 'rails-erd'  ,        '~> 1.1.0'
  gem 'capistrano',         '~> 3.4'
  gem 'capistrano-bundler', '~> 1.1'
  gem 'capistrano-rails',   '~> 1.1'

  gem 'stackprof'
  gem 'flamegraph'

  gem 'ruby-prof'

  # rake i18n:sort to sort locale files
  gem 'i18n_yaml_sorter'
  gem 'i18n-tasks', '~> 0.9'
end


group :development, :test do
  # gem 'jasmine-rails'
end

group :production, :staging do
  gem 'execjs',           '~> 2.2.1'
  gem 'therubyracer',     '~> 0.12.1'
end

gem 'rack-mini-profiler', '~> 0.9.2', :require => false
#-------------------------------------------------------------------------------
# Devs: if you want to alter your PERSONAL setup, on your own machine, create a
# Gemfile.local.rb and put stuff in there.
# This should be used to tweak development or test groups in a way that doesn't
# affect other people.
# e.g. include your favourite debugger/profiler/ide-integrations here.
#
local_gemfile = File.dirname(__FILE__) + "/Gemfile.local.rb"
if File.file?(local_gemfile)
  self.instance_eval(Bundler.read_file(local_gemfile))
end
