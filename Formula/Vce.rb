class Vce < Formula
  desc "Randroid's Text to Voice Script. Using OpenAI's API."
  homepage "https://github.com/randroid88/homebrew-vce"
  url "https://github.com/randroid88/homebrew-vce/archive/refs/tags/1.0.2.tar.gz"
  sha256 "adacad46b6a4380659c8cfee43b6e76c04c2580ed8eba41ccb064968b0dcdcaf"

  # uses_from_macos "python@3"

  def install
    libexec.install Dir["*.py"]

    # Write a wrapper script and install it to bin
    (bin/"vce").write <<~EOS
      #!/bin/bash
      /usr/bin/env python3 "#{libexec}/vce.py" "$@"
    EOS
  end

  test do
    system "#{bin}/vce"
  end
end