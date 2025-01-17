
(howto-integrate-virtual-keyboard)=
# How to integrate a client-side virtual keyboard

The Anbox Streaming SDK enables developers to build a hybrid mobile application that can integrate the features that Anbox Cloud provides. It comes with an [Android library](https://developer.android.com/studio/projects/android-library) that offers easy-to-use native components like Anbox WebView, which extends the AOSP [WebView](https://developer.android.com/reference/android/webkit/WebView). It provides better handling of text input for the hybrid application that loads the Anbox Streaming JavaScript SDK with an embedded WebView for video streaming.

You can use Anbox WebView to quickly integrate a client-side virtual keyboard feature into your mobile application. This client-side virtual keyboard can send text to the Android container on the fly when typing:

* When the text editor of the application in the instance gains focus, the client-side virtual keyboard pops up, and it disappears when the focus moves away.
* When typing on the client-side virtual keyboard, the input text is sent to the Android container and displayed in the running application.

The following steps provide general instructions for integrating the client-side virtual keyboard feature into an Android application. See [customizing the virtual keyboard](#customizing-the-virtual-keyboard) for additional implementation options.

For the complete implementation details, refer to the `enhanced_webview_streaming` example in the `example/android` folder.

```{note}
To enable the app running in the Android container to receive the texts sent from the client-side virtual keyboard, you must declare the feature `enable_anbox_ime` in the application manifest file when creating an application.
```

## Import the AAR library

Check out the [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk) from GitHub:

    git clone https://github.com/canonical/anbox-streaming-sdk.git

The `android/libs` folder contains the `com.canonical.anbox.streaming_sdk.aar` AAR file. See the official [documentation](https://developer.android.com/studio/projects/android-library) for how to import an Android library into an Android application project.

The `examples/android` folder contains the `enhanced_webview_streaming` Android application. Refer to this application as an example for this feature integration.

## Integrate components

After importing the AAR file, add the `AnboxWebView` element to the activity layout file and adjust its layout to your needs. For example:

   ```
    <com.canonical.anbox.streaming_sdk.AnboxWebView
        android:id="@+id/webview"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
   ```

## Build communication bridge

In your web application code, define the JavaScript functions that can be invoked from the Android Java layer (Anbox WebView). Those functions are just wrappers of the APIs that are exposed from the JavaScript SDK.

Adding the following JavaScript code snippet builds up a communication tunnel between the Android Java layer (Anbox WebView) and the JavaScript layer. It attaches the `AnboxStream` object to the global `window` object. The functions will automatically be invoked by the Android Java layer (Anbox WebView).

   ```
   <script type="module">
     import {AnboxStream} from './js/anbox-stream-sdk.js';
     window.stream = new AnboxStream({
     ...
     ...
     ...
     });
   </script>
   <script>
     function sendIMECommittedText(text) {
       window.stream.sendIMECommittedText(text);
     }
     function sendIMEComposingText(text) {
       window.stream.sendIMEComposingText(text);
     }
     function sendIMETextDeletion(counts) {
       window.stream.sendIMETextDeletion(counts);
     }
     function sendIMEAction(name, params) {
       window.stream.sendIMEAction(name, params);
     }
     function sendIMEComposingRegion(start, end) {
       window.stream.sendIMEComposingRegion(start, end);
     }
   </script>
   ```

## Customizing the virtual keyboard

You can take advantage of the interfaces that the Anbox WebView exposes to provide your own implementation of a client-side virtual keyboard that customizes:

* Input text processing
* Handling of state changes of the virtual keyboard

1. Set up the listener to the activity for which you want to capture the text input events from the virtual keyboard or monitor its visibility changes during streaming.
   ```
   import com.canonical.anbox.streaming_sdk.AnboxWebView;
   ...
   public class MainActivity extends AppCompatActivity implements AnboxWebView.VirtualKeyboardListener {
   ...
       protected void onCreate(Bundle savedInstanceState) {
           ...
           mWebview = (AnboxWebView) findViewById(R.id.webview);
           mWebview.setVirtualKeyboardListener(this);
           ...
       }
   ```

2. When people start typing, one of the following methods from the `AnboxWebView.VirtualKeyboardListener` interfaces will be triggered. Implement the following methods for the `AppInterface.ActionListener` interfaces so that the application can respond to those events and send texts to the Android container:

   ```
       /**
        * Called as text is committed from the virtual keyboard.
        *
        * @param text the committed text displayed in the text editor after its composing state
        *        is cleared.
        * @note  text is not the whole visual characters displaying in the text editor, instead it's
        *        just the new text appended to the current existing text after finishing composing.
        *
        */
       @Override
       public void onVirtualKeyboardTextCommitted(String text) {
       }
   ```

   ```
       /**
        * Called as text is being composing from the virtual keyboard.
        *
        * @param text the composing text displayed in the virtual keyboard.
        * @note  There might be no composing state for some CJK language based IMEs, hence
        *        this function may not be called at all for those languages in some IMEs.
        *
        */
       @Override
       public void onVirtualKeyboardTextComposing(String text) {
       }
   ```

   ```
       /**
        * Called as input text is deleted from the current text editor.
        *
        * @param counts the number of characters that are deleted before the current cursor position.
        */
       @Override
       public void onVirtualKeyboardTextDeleted(int counts) {
       }
   ```

   ```
       /**
        * Called as the region of composing text is changed.
        *
        * @param start the position in the text at which the composing region begins.
        * @param end the position in the text at which the composing region ends.
        */
       @Override
       public void onVirtualKeyboardComposingTextRegionChanged(int start, int end) {
       }
   ```

   ```
       /**
        * Called as the state of the virtual keyboard is changed.
        *
        * @param visible the visibility of the virtual keyboard, true or false.
        * @param heightRatio the ratio of virtual keyboard's height to screen when virtual keyboard is visible.
        *        This can be used to notify the IME running in the Android container
        *        to adjust the display height to honor the virtual keyboard display
        *        ratio on the client side.
        *
        */
       @Override
       public void onVirtualKeyboardStateChanged(boolean visible, double displayRatio) {
       }
   ```

3. Once the virtual keyboard pops up on the client side, the `onVirtualKeyboardStateChanged` callback function is triggered. To keep the display proportions correct for IME displaying on both the client and the server ends, the `show` action, which carries the display ratio, must be sent out to the server side.

   Similarly, when the virtual keyboard pops down on the client side, you must ensure that the behavior of the virtual keyboard is synced on both ends. Therefore, the `hide` action must be sent out to the server side.


   ```
       @Override
       public void onVirtualKeyboardStateChanged(boolean visible, double displayRatio) {
           if (visible == true) {
               String action = "show";
               String params = "height-ratio=" + displayRatio;
               mWebView.loadUrl(String.format("javascript:sendIMEAction(\"%s\", \"%s\")", action, params));
           } else  {
               String action = "hide";
               mWebView.loadUrl(String.format("javascript:sendIMEAction(\"%s\")", action));
           }
       }
   ```

4. When typing on the virtual keyboard, a text input event is triggered when one of the following scenarios occurs:
   - A series of characters is committed to a text editor
   - A text is currently being composed
   - A text is being deleted

    In the above cases, the changed text must be sent to the server side through the JavaScript SDK. This can be done by calling JavaScript functions that are defined in HTML through Anbox WebView. For example, for committing text:

   ```
       @Override
       public void onVirtualKeyboardTextCommitted(String text) {
           mWebView.loadUrl(String.format("javascript:sendIMECommittedText(\"%s\")", text));
       }
   ```
