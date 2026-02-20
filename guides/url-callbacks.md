# URL Callbacks Guide (x-callback-url)

Use this guide to integrate Alter with other apps using URL schemes.

## Video Tutorial

- https://www.youtube.com/watch?v=X-XJiveQ-Wc

## Introduction

Alter supports x-callback-url so apps can trigger actions in each other.
You can:

- trigger Alter actions from external apps
- trigger external app actions from Alter
- pass input data in URLs
- return back to the originating app (depending on app support)

## How It Works

1. Trigger Alter actions from another app via `alter://...` URLs.
2. Trigger external app actions from Alter using that app's URL scheme.

## Trigger Alter Actions From External Apps

1. Open Action Editor.
2. Select an action.
3. In `General`, copy the URL from the **URL Callback** section.
4. Paste the URL into another app (browser, notes, shortcuts, etc.).

![Alter Callback URLs](https://alterhq.com/assets-doc/images/integrations/alter-callback-urls-focus.webp)

## Trigger External App Actions From Alter

1. Create a clickable URL in Alter using the target app scheme.
2. Format parameters exactly as required by that app.
3. Click to run and verify action behavior.

## Examples

### Alter callback examples

- Search query:
  - `alter://action/ask-web?input=What+is+Alter+MacOS`
  - [alter://action/ask-web?input=What+is+Alter+MacOS](alter://action/ask-web?input=What+is+Alter+MacOS)

- Business strategist without input:
  - `alter://action/business-strategist-gpt`
  - [alter://action/business-strategist-gpt](alter://action/business-strategist-gpt)

- Business strategist with input:
  - `alter://action/business-strategist-gpt?input=Explain+Red+Ocean+Strategy`
  - [alter://action/business-strategist-gpt?input=Explain+Red+Ocean+Strategy](alter://action/business-strategist-gpt?input=Explain+Red+Ocean+Strategy)

### Cross-app example

- Bear note creation:
  - `bear://x-callback-url/create?title=Demo%20Note`

## Supported Apps (Sampling)

Apps with x-callback-url or URL-scheme support include:

- [1Writer](http://1writerapp.com/developers)
- [2Do](http://2doapp.com/kb/article/url-scheme-supported-by-2do-for-apps-like-launch-center-pro.html)
- [Agenda](https://agenda.community/t/x-callback-url-support-and-reference/27253)
- [Appigo Todo](http://support.appigo.com/support/solutions/articles/179661-third-party-integration-with-todo-ios-apps)
- [Bear](https://bear.app/faq/X-callback-url%20Scheme%20documentation/)
- [Begin](http://blog.beginapp.co/blog/2013/9/15/url-schemes)
- [breadwallet](http://breadwallet.com)
- [Byword](http://bywordapp.com/support/url-scheme.html)
- [Cal2Todo](http://yaas4home.blog.fc2.com/blog-entry-344.html)
- [ClouDrop](http://shabz.co/m/dev.html)
- [Command-C](http://danilo.to/command-c/faq/how-to-use-x-callback-url)
- [Daedalus Touch](http://daedalusapp.com/url-scheme/)
- [Daymate](http://www.nodheadsoftware.com/daymate/x-callback-url/)
- [Definition](http://handleopenurl.com/scheme/definition)
- [DEVONThink](https://www.devontechnologies.com/redirect/apps/devonthink)
- [Dispatch](http://www.dispatchapp.net)
- [Drafts](http://getdrafts.com)
- [Due](http://www.dueapp.com/developer.html)
- [Editorial](http://omz-software.com/editorial/docs/ios/editorial_urlscheme.html)
- [Equipd Bible](http://www.equipd.me/kb/url-scheme/)
- [Fantastical](http://flexibits.com/fantastical-iphone/faq)
- [Gladys](http://www.bru.build/gladys-callback-scheme)
- [Google Chrome](https://developers.google.com/chrome/mobile/docs/ios-links)
- [Google Maps](http://philgr.com/blog/google-maps-and-x-callback-url-support)
- [Hook](https://hookproductivity.com/)
- [iCab Mobile](http://www.icab.de/blog/2012/07/01/icab-mobile-6-0-supports-x-callback-url/)
- [Instapaper](http://blog.instapaper.com/post/4637427075)
- [iPGMail](http://ipgmail.com/info/developers/)
- [iZettle](http://developer.izettle.com/)
- [Kippster for Kippt](http://kippster.net/url-schemes/)
- [Launch Center Pro](http://appcubby.com/launch-center/)
- [miCal](http://micalapp.com/en/faqs#category_10)
- [Missives](http://blackfoggames.com/Missives/callback.html)
- [Multitimer](http://persapps.com/app/multitimer/url-scheme.php)
- [MyDoorOpener](http://forums.mydooropener.com/viewtopic.php?f=16&t=295)
- [Notesy](http://notesy-app.com/weblog/files/b7e15801e5b4448495eaaccfdb374cc7-20.html)
- [OmniFocus](https://discourse.omnigroup.com/t/automation-in-omnifocus-2-14-released-2016-04-26/23985/92)
- [Opener](http://www.opener.link/api)
- [Otto's Remote](http://andymolloy.net/blog/2013/08/21/otto-and-x-callback-url/)
- [Overcast](https://overcast.fm)
- [Pleco](http://www.pleco.com/ipmanual/vershist.html)
- [Poster](http://www.tomwitkin.com/poster/developers/)
- [Prizmo](https://github.com/creaceed/PrizmoAPI)
- [Procraster](http://procrasterapp.com/userguide/51)
- [RollPG](http://blackfoggames.com/RollPG/callback.html)
- [RunJavascript](https://itunes.apple.com/us/app/runjavascript/id1254402852)
- [Scanner Go](http://ilevelupapps.com/scanner-go)
- [Shopi](http://sapient-pair.com/shopi/automation.html)
- [Showrtpath Browser](http://showrtpath.hatenablog.com/entry/2014/01/04/085804)
- [Silo](https://siloapp.net/developer)
- [Shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios)
- [Story Planner](http://literautas.com/en/apps/story-planner/x-callback-url/)
- [Streets](http://www.futuretap.com/blog/streets-api/)
- [Terminology](http://agiletortoise.com/developers/terminology)
- [TextCenter](http://textcenterapp.com/xcallback.html)
- [TextExpander Touch](http://smile.clarify-it.com/d/ehf7a4)
- [Textastic](http://www.textasticapp.com/v4/manual/x-callback-url.html)
- [Textkraft](http://www.infovole.de/en/support-en/x-callback-url-in-textkraft/)
- [TextTool](http://blackfoggames.com/TextTool/callback.html)
- [Things](https://culturedcode.com/things/help/url-scheme/)
- [Timepage](http://moleskine.helpscoutdocs.com/article/92-timepage-url-scheme)
- [Trello](https://trello.com/c/cJfzOdDm/188-automate-with-url-scheme)
- [Tumblr for iOS](https://github.com/tumblr/TMTumblrSDK#url-schemes)
- [Ulysses](http://ulyssesapp.com/kb/x-callback-url/)
- [UpwardNotes](http://www.upwordnotes.com/url-scheme/)
- [VideoLAN](https://wiki.videolan.org/Documentation:IOS/#x-callback-url)
- [Waterminder](https://funnmedia.zendesk.com/hc/en-us/articles/360007745191-WaterMinder-X-Callback-URL-Support)
- [Where To?](http://www.futuretap.com/api/whereto/)
- [Working Copy](http://workingcopyapp.com/x-callback-url.html)

## Testing And Troubleshooting

- Verify the URL scheme and parameters.
- URL-encode special characters.
- Confirm the target app supports the action.
- Paste the app's callback documentation URL into Alter to ground syntax/rules.

## Related Docs

- https://alterhq.com/docs#alter-actions-workflows
- https://alterhq.com/docs#troubleshooting-integrations
