source "https://rubygems.org"

gem "rake", "10.3.2"

gem "padrino", "0.12.4"

gem "jruby-openssl", "0.9.5"

gem "orchestrate", "0.9.1"

gem "puma", "2.9.2"

gem "committee", "1.5.2"

group :development do
    gem "dotenv", "1.0.2"

    gem "better_errors", "2.0.0"
    # gem "binding_of_caller", "0.7.3.pre1"
end

group :development, :test do
    gem "prmd", github: "interagent/prmd", ref: "d2897"
end

group :test do
    gem "rr", "1.1.2", require: false

    gem "rspec", "3.1.0"

    gem "rack-test", "0.6.2", require: "rack/test"

    gem "vcr", "2.9.3"
    gem "webmock", "1.20.2"

    gem "ruby-lint", "2.0.2"
    gem "rubocop", "0.27.0"

    gem "simplecov", "0.9.1", require: false
    gem "coveralls", "0.7.1", require: false
    gem "codeclimate-test-reporter", "0.4.1", require: false
    gem "simplecov-summary", require: false, github: "inossidabile/simplecov-summary", ref: "e140a"
end
