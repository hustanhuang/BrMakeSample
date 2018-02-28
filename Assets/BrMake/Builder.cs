#if UNITY_EDITOR
using System.IO;
using UnityEditor;
using UnityEngine;

namespace BrMake
{
    public class Builder : MonoBehaviour
    {
        private static void BuildIos()
        {
            var options = new BuildPlayerOptions
            {
                scenes = new[]
                {
                    "Assets/Main.unity"
                },
                locationPathName = Directory.GetCurrentDirectory() + "/Build/stage1",
                target = BuildTarget.iOS
            };

            BuildPipeline.BuildPlayer(options);
        }
    }
}
#endif