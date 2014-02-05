require 'spec_helper'
require 'thing'
require 'capybara/poltergeist'
Capybara.javascript_driver = :poltergeist

describe "something" do
  it "does something" do
    This.new.foo.should be_true
  end
end
