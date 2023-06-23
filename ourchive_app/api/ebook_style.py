def get_epub_style():
	return r""" /* Based on Standard Ebooks stylesheet */

		body{
			font-variant-numeric: oldstyle-nums;
			hyphens: auto;
			-epub-hyphens: auto;
		}

		p{
			margin: 0;
			text-indent: 1em;
		}

		hr{
			border: none;
			border-top: 1px solid;
			height: 0;
			margin: 1.5em auto;
			width: 25%;
		}

		q::before,
		q::after{
			content: "";
		}

		blockquote{
			margin: 1em 2.5em;
		}

		h1,
		h2,
		h3,
		h4,
		h5,
		h6,
		hgroup{
			break-after: avoid;
			break-inside: avoid;
			font-variant: small-caps;
			hyphens: none;
			-epub-hyphens: none;
			margin: 3em 0;
			text-align: center;
		}

		hgroup > *{
			font-weight: normal;
			margin: 0;
		}

		hgroup > *:first-child{
			font-weight: bold;
		}

		p.continued,
		h2 + p,
		h3 + p,
		h4 + p,
		h5 + p,
		h6 + p,
		header + p,
		hr + p,
		hgroup + p,
		p:first-child{
			hanging-punctuation: first last;
			text-indent: 0;
		}

		cite{
			font-style: normal;
		}

		abbr{
			border: none;
			white-space: nowrap;
		}

		blockquote cite{
			display: block;
			font-style: italic;
			text-align: right;
		}

		blockquote cite i{
			font-style: normal;
		}

		b,
		strong{
			font-variant: small-caps;
			font-weight: normal;
		}

		i > i,
		em > i,
		i > em{
			font-style: normal;
		}

		ol,
		ul{
			margin-bottom: 1em;
			margin-top: 1em;
		}

		header{
			break-after: avoid;
			break-inside: avoid;
			hyphens: none;
			-epub-hyphens: none;
			text-align: center;
		}

		header > * + p{
			text-indent: 0;
		}

		article > header + *,
		section > header + *{
			margin-top: 3em;
		}

		a[epub|type~="noteref"]{
			font-size: .75em;
			font-style: normal !important;
			vertical-align: super;
		}

		section[epub|type~="endnotes"] > ol > li{
			margin: 1em 0;
		}

		/* Invert images in dark mode. RMSDK requires a target media as well as a state. */
		@media all and (prefers-color-scheme: dark){
			img[epub|type~="se:image.color-depth.black-on-transparent"]{
				filter: invert(100%);
			}

			img[epub|type~="se:image.color-depth.black-on-transparent"][epub|type~="se:image.style.realistic"]{
				background: currentColor;
				filter: none;
			}
		}"""