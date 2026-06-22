using Archipelago.MultiClient.Net.MessageLog.Messages;
using BepInEx;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using UnityEngine;

namespace SpiritValleyArchipelagoClient.Archipelago;

// shamelessly stolen from oc2-modding https://github.com/toasterparty/oc2-modding/blob/main/OC2Modding/GameLog.cs
public static class ArchipelagoConsole
{
    public static bool Hidden = true;

    private static List<string> logLines = new();
    private static Vector2 scrollView;
    private static Rect window;
    private static Rect scroll;
    private static Rect text;
    private static Rect hideShowButton;

    private static GUIStyle textStyle = new();
    private static string scrollText = "";
    private static float lastUpdateTime = Time.time;
    private const int MaxLogLines = 80;
    private const float HideTimeout = 15f;

    private static string CommandText = "!help";
    private static Rect CommandTextRect;
    private static Rect SendCommandButton;

    public static void Awake()
    {
        UpdateWindow();
    }

    public static void LogArchMessage(LogMessage msg)
    {
        if (msg.ToString().IsNullOrWhiteSpace()) return;

        switch (msg)
        {
            case HintItemSendLogMessage hintmsg:
                if (hintmsg.IsRelatedToActivePlayer)
                {

                    if (hintmsg.Parts.Length == 1)
                    {
                        LogMessage(hintmsg.Parts[0].Text);
                        break;
                    }

                    var builder = new StringBuilder();
                    foreach (var part in hintmsg.Parts)
                    {
                        if ((int)part.Type == 1)//player part type
                        {
                            builder.Append($"<color=#{part.Color.R:x2}{part.Color.G:x2}{part.Color.B:x2}ff>");
                            builder.Append(part.Text);
                            builder.Append("</color>");
                        }
                        else if ((int)part.Type == 2)//item part type
                        {
                            builder.Append($"<color=#{part.Color.R:x2}{part.Color.G:x2}{part.Color.B:x2}ff>");
                            builder.Append(part.Text);
                            builder.Append("</color>");
                        }
                        else if ((int)part.Type == 3)//location part type
                        {
                            builder.Append($"<color=#{part.Color.R:x2}{part.Color.G:x2}{part.Color.B:x2}ff>");
                            builder.Append(part.Text);
                            builder.Append("</color>");
                        }
                        else
                        {
                            builder.Append(part.Text);
                        }
                    }

                    LogMessage(builder.ToString());
                }
                break;

            case ItemSendLogMessage itemmsg:
                if (itemmsg.IsRelatedToActivePlayer)
                {

                    if (itemmsg.Parts.Length == 1)
                    {
                        LogMessage(itemmsg.Parts[0].Text);
                        break;
                    }

                    var builder = new StringBuilder();
                    foreach (var part in itemmsg.Parts)
                    {
                        if ((int)part.Type == 1)//player part type
                        {
                            builder.Append($"<color=#{part.Color.R:x2}{part.Color.G:x2}{part.Color.B:x2}ff>");
                            builder.Append(part.Text);
                            builder.Append("</color>");
                        }
                        else if ((int)part.Type == 2)//item part type
                        {
                            builder.Append($"<color=#{part.Color.R:x2}{part.Color.G:x2}{part.Color.B:x2}ff>");
                            builder.Append(part.Text);
                            builder.Append("</color>");
                        }
                        else if ((int)part.Type == 3)//location part type
                        {
                            builder.Append($"<color=#{part.Color.R:x2}{part.Color.G:x2}{part.Color.B:x2}ff>");
                            builder.Append(part.Text);
                            builder.Append("</color>");
                        }
                        else
                        {
                            builder.Append(part.Text);
                        }
                    }

                    LogMessage(builder.ToString());
                }
                break;


        }

    }

    public static void LogMessage(string message)
    {
        if (message.IsNullOrWhiteSpace()) return;

        if (logLines.Count == MaxLogLines)
        {
            logLines.RemoveAt(0);
        }
        logLines.Add(message);
        SpiritValleyArchipelago.BepinLogger.LogMessage(message);
        lastUpdateTime = Time.time;
        UpdateWindow();
    }

    public static void LogDebug(string message)
    {
        if (message.IsNullOrWhiteSpace()) return;
        SpiritValleyArchipelago.BepinLogger.LogMessage(message);
    }

    public static void LogError(string message)
    {
        if (message.IsNullOrWhiteSpace()) return;
        LogMessage(message);
        if (Hidden) { toggleConsole(); }
    }

    public static void OnGUI()
    {
        if (logLines.Count == 0) return;

        if (!Hidden || Time.time - lastUpdateTime < HideTimeout)
        {
            scrollView = GUI.BeginScrollView(window, scrollView, scroll);
            GUI.Box(text, "");
            GUI.Box(text, scrollText, textStyle);
            GUI.EndScrollView();
        }

        //if (GUI.Button(hideShowButton, Hidden ? "Show" : "Hide"))
        //{
        //    Hidden = !Hidden;
        //    UpdateWindow();
        //}

        // draw client/server commands entry
        if (Hidden || !ArchipelagoClient.Authenticated) return;

        CommandText = GUI.TextField(CommandTextRect, CommandText);
        if (!CommandText.IsNullOrWhiteSpace() && GUI.Button(SendCommandButton, "Send"))
        {
            SpiritValleyArchipelago.ArchipelagoClient.SendMessage(CommandText);
            CommandText = "";
        }
    }

    public static void toggleConsole()
    {
        Hidden = !Hidden;
        UpdateWindow();
    }

    public static void UpdateWindow()
    {
        scrollText = "";

        if (Hidden)
        {
            if (logLines.Count > 0)
            {
                scrollText = logLines[logLines.Count - 1];
            }
        }
        else
        {
            for (var i = 0; i < logLines.Count; i++)
            {
                scrollText += "> ";
                scrollText += logLines.ElementAt(i);
                if (i < logLines.Count - 1)
                {
                    scrollText += "\n\n";
                }
            }
        }

        var width = (int)(Screen.width * 0.4f);
        int height;
        int scrollDepth;
        if (Hidden)
        {
            height = (int)(Screen.height * 0.03f);
            scrollDepth = height;
        }
        else
        {
            height = (int)(Screen.height * 0.3f);
            scrollDepth = height * 10;
        }

        window = new Rect(Screen.width / 2 - width / 2, 0, width, height);
        scroll = new Rect(0, 0, width * 0.9f, scrollDepth);
        scrollView = new Vector2(0, scrollDepth);
        text = new Rect(0, 0, width, scrollDepth);

        textStyle.alignment = TextAnchor.LowerLeft;
        textStyle.fontSize = Hidden ? (int)(Screen.height * 0.0165f) : (int)(Screen.height * 0.0185f);
        textStyle.normal.textColor = Color.white;
        textStyle.richText = true;
        textStyle.wordWrap = !Hidden;

        var xPadding = (int)(Screen.width * 0.01f);
        var yPadding = (int)(Screen.height * 0.01f);

        textStyle.padding = Hidden
            ? new RectOffset(xPadding / 2, xPadding / 2, yPadding / 2, yPadding / 2)
            : new RectOffset(xPadding, xPadding, yPadding, yPadding);

        var buttonWidth = (int)(Screen.width * 0.12f);
        var buttonHeight = (int)(Screen.height * 0.03f);

        hideShowButton = new Rect(Screen.width / 2 + width / 2 + buttonWidth / 3, Screen.height * 0.004f, buttonWidth,
            buttonHeight);

        // draw server command text field and button
        width = (int)(Screen.width * 0.4f);
        var xPos = (int)(Screen.width / 2.0f - width / 2.0f);
        var yPos = (int)(Screen.height * 0.307f);
        height = (int)(Screen.height * 0.022f);

        CommandTextRect = new Rect(xPos, yPos, width, height);

        width = (int)(Screen.width * 0.035f);
        yPos += (int)(Screen.height * 0.03f);
        SendCommandButton = new Rect(xPos, yPos, width, height);
    }
}