# What

A simple command line util for pasting in some text and having it read it out loud.

# How

## Getting the util

This is setup as a brew tap so it can be installed like this:

`brew tap randroid88/vce`

`brew install vce`

## Running the util
`
vce --text "Some text that you want to be spoken outloud" --api-key "Your OpenAI API Key if you haven't set OPENAI_API_KEY"
`

Both arguments are optional.
If you don't pass in the text, you will be prompted for it.
If you don't want to pass in your api-key, you can set OPENAI_API_KEY in your env.

**Tip:** _You can include multiple lines of text. Just be sure to wrap in quotes when passing in as an argument.
When entering text after being prompted, be sure to finish by pressing Return twice (e.g.
finish on a newline)._
