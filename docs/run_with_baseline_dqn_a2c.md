
#### ➡️ Index
- []()
- []()

---

# Python API를 사용하여 예제 알고리즘 (DQN, A2C)로 학습하기

> 기본적으로 제공하는 DQN, A2C Baseline Code 실행을 위한 가이드 페이지 입니다.
> python API로 제출할 경우 Baseline으로 제공하는 경로들을 따라 주시기 바랍니다.

## Baseline setting.
- 먼저, 대회 깃허브 페이지에서 Baseline Code들을 경로에 맞게 다운로드 해주시기 바랍니다.
  - [Baseline Code](https://github.com/reinforcement-learning-kr/2021_RLKR_Drone_Delivery_Challenge_with_Unity/tree/master/baseline)를 참고해주세요 !

## Directory 설명.
```bash
├─code
│  ├─best_model
│  └─__pycache__
└─RL_Drone
    ├─DroneDelivery_Data
    │  ├─Managed
    │  ├─ML-Agents
    │  │  └─Timers
    │  ├─Plugins
    │  │  └─x86_64
    │  ├─Resources
    │  └─StreamingAssets
    │      └─Inference_Data
    └─MonoBleedingEdge
        ├─EmbedRuntime
        └─etc
            └─mono
                ├─2.0
                │  └─Browsers
                ├─4.0
                │  └─Browsers
                ├─4.5
                │  └─Browsers
                └─mconfig
```
- 크게 2가지 폴더로 나누어져 있습니다.
  - code: python script와 model 관리를 위한 파일과 폴더가 있습니다.
  - RL_Drone: 환경과 관련된 유니티 파일과 폴더가 있습니다. 다운로드 받은 환경 zip파일을 RL_Drone 폴더에 압축해제 하시기 바랍니다.
### code 폴더.
```bash
└─code
  │  Agent_a2c.py
  │  Agent_dqn.py
  │  Agent_user.py
  │  Drone_gym.py
  │  inference.py
  │
  └─best_model
        best_model.pkl
```
- Agent_a2c.py: a2c 알고리즘 기반 python script 입니다.
- Agent_dqn.py: dqn 알고리즘 기반 python script 입니다.
- Agent_user.py: Agent Class의 기본 형태를 가지고 있는 python script 입니다.
- Drone_gym.py: 원활한 대회 진행을 위해 OpenAI gym 스타일로 변환된 Drone gym 입니다.
- inference.py: 서버에서 진행되는 evaluation 진행 예시 입니다.
- best_model: model이 저장되는 경로 입니다.

### RL_Drone
```bash
─RL_Drone
    │  DroneDelivery.exe
    │  UnityCrashHandler64.exe
    │  UnityPlayer.dll
    │
    ├─DroneDelivery_Data
    │  │  app.info
    │  │  boot.config
    │  │  globalgamemanagers
    │  │  globalgamemanagers.assets
    │  │  level0
    │  │  level0.resS
    │  │  resources.assets
    │  │  resources.assets.resS
    │  │  RuntimeInitializeOnLoads.json
    │  │  ScriptingAssemblies.json
    │  │  sharedassets0.assets
    │  │  sharedassets0.assets.resS
    │  │  sharedassets0.resource
    │  │
    │  ├─Managed
    │  │      Assembly-CSharp.dll
    │  │      Google.Protobuf.dll
    │  │      Grpc.Core.dll
    │  │      Mono.Security.dll
    │  │      mscorlib.dll
    │  │      netstandard.dll
    │  │      Newtonsoft.Json.dll
    │  │      PA_DronePack.dll
    │  │      System.ComponentModel.Composition.dll
    │  │      System.Configuration.dll
    │  │      System.Core.dll
    │  │      System.Data.dll
    │  │      System.Diagnostics.StackTrace.dll
    │  │      System.dll
    │  │      System.Drawing.dll
    │  │      System.EnterpriseServices.dll
    │  │      System.Globalization.Extensions.dll
    │  │      System.Interactive.Async.dll
    │  │      System.IO.Abstractions.dll
    │  │      System.IO.Abstractions.TestingHelpers.dll
    │  │      System.IO.Compression.dll
    │  │      System.IO.Compression.FileSystem.dll
    │  │      System.Net.Http.dll
    │  │      System.Numerics.dll
    │  │      System.Runtime.dll
    │  │      System.Runtime.Serialization.dll
    │  │      System.Runtime.Serialization.Xml.dll
    │  │      System.ServiceModel.Internals.dll
    │  │      System.Transactions.dll
    │  │      System.Xml.dll
    │  │      System.Xml.Linq.dll
    │  │      System.Xml.XPath.XDocument.dll
    │  │      Unity.Barracuda.BurstBLAS.dll
    │  │      Unity.Barracuda.dll
    │  │      Unity.Barracuda.ONNX.dll
    │  │      Unity.Burst.dll
    │  │      Unity.Burst.Unsafe.dll
    │  │      Unity.Mathematics.dll
    │  │      Unity.ML-Agents.CommunicatorObjects.dll
    │  │      Unity.ML-Agents.dll
    │  │      Unity.ML-Agents.Extensions.dll
    │  │      Unity.ML-Agents.Extensions.Input.dll
    │  │      Unity.TextMeshPro.dll
    │  │      Unity.Timeline.dll
    │  │      Unity.VisualScripting.Antlr3.Runtime.dll
    │  │      Unity.VisualScripting.Core.dll
    │  │      Unity.VisualScripting.Flow.dll
    │  │      Unity.VisualScripting.State.dll
    │  │      UnityEngine.AccessibilityModule.dll
    │  │      UnityEngine.AIModule.dll
    │  │      UnityEngine.AndroidJNIModule.dll
    │  │      UnityEngine.AnimationModule.dll
    │  │      UnityEngine.ARModule.dll
    │  │      UnityEngine.AssetBundleModule.dll
    │  │      UnityEngine.AudioModule.dll
    │  │      UnityEngine.ClothModule.dll
    │  │      UnityEngine.ClusterInputModule.dll
    │  │      UnityEngine.ClusterRendererModule.dll
    │  │      UnityEngine.CoreModule.dll
    │  │      UnityEngine.CrashReportingModule.dll
    │  │      UnityEngine.DirectorModule.dll
    │  │      UnityEngine.dll
    │  │      UnityEngine.DSPGraphModule.dll
    │  │      UnityEngine.GameCenterModule.dll
    │  │      UnityEngine.GIModule.dll
    │  │      UnityEngine.GridModule.dll
    │  │      UnityEngine.HotReloadModule.dll
    │  │      UnityEngine.ImageConversionModule.dll
    │  │      UnityEngine.IMGUIModule.dll
    │  │      UnityEngine.InputLegacyModule.dll
    │  │      UnityEngine.InputModule.dll
    │  │      UnityEngine.JSONSerializeModule.dll
    │  │      UnityEngine.LocalizationModule.dll
    │  │      UnityEngine.ParticleSystemModule.dll
    │  │      UnityEngine.PerformanceReportingModule.dll
    │  │      UnityEngine.Physics2DModule.dll
    │  │      UnityEngine.PhysicsModule.dll
    │  │      UnityEngine.ProfilerModule.dll
    │  │      UnityEngine.RuntimeInitializeOnLoadManagerInitializerModule.dll
    │  │      UnityEngine.ScreenCaptureModule.dll
    │  │      UnityEngine.SharedInternalsModule.dll
    │  │      UnityEngine.SpriteMaskModule.dll
    │  │      UnityEngine.SpriteShapeModule.dll
    │  │      UnityEngine.StreamingModule.dll
    │  │      UnityEngine.SubstanceModule.dll
    │  │      UnityEngine.SubsystemsModule.dll
    │  │      UnityEngine.TerrainModule.dll
    │  │      UnityEngine.TerrainPhysicsModule.dll
    │  │      UnityEngine.TextCoreModule.dll
    │  │      UnityEngine.TextRenderingModule.dll
    │  │      UnityEngine.TilemapModule.dll
    │  │      UnityEngine.TLSModule.dll
    │  │      UnityEngine.UI.dll
    │  │      UnityEngine.UIElementsModule.dll
    │  │      UnityEngine.UIElementsNativeModule.dll
    │  │      UnityEngine.UIModule.dll
    │  │      UnityEngine.UmbraModule.dll
    │  │      UnityEngine.UNETModule.dll
    │  │      UnityEngine.UnityAnalyticsModule.dll
    │  │      UnityEngine.UnityConnectModule.dll
    │  │      UnityEngine.UnityCurlModule.dll
    │  │      UnityEngine.UnityTestProtocolModule.dll
    │  │      UnityEngine.UnityWebRequestAssetBundleModule.dll
    │  │      UnityEngine.UnityWebRequestAudioModule.dll
    │  │      UnityEngine.UnityWebRequestModule.dll
    │  │      UnityEngine.UnityWebRequestTextureModule.dll
    │  │      UnityEngine.UnityWebRequestWWWModule.dll
    │  │      UnityEngine.VehiclesModule.dll
    │  │      UnityEngine.VFXModule.dll
    │  │      UnityEngine.VideoModule.dll
    │  │      UnityEngine.VirtualTexturingModule.dll
    │  │      UnityEngine.VRModule.dll
    │  │      UnityEngine.WindModule.dll
    │  │      UnityEngine.XRModule.dll
    │  │
    │  ├─ML-Agents
    │  │  └─Timers
    │  │          TrainScene_timers.json
    │  │
    │  ├─Plugins
    │  │  └─x86_64
    │  │          grpc_csharp_ext.x64.dll
    │  │          lib_burst_generated.dll
    │  │          lib_burst_generated.txt
    │  │
    │  ├─Resources
    │  │      unity default resources
    │  │      unity_builtin_extra
    │  │
    │  └─StreamingAssets
    │      │  Parameters.json
    │      │
    │      └─Inference_Data
    │              Easy.json
    │              Normal.json
    │
    └─MonoBleedingEdge
        ├─EmbedRuntime
        │      mono-2.0-bdwgc.dll
        │      MonoPosixHelper.dll
        │
        └─etc
            └─mono
                │  browscap.ini
                │  config
                │
                ├─2.0
                │  │  DefaultWsdlHelpGenerator.aspx
                │  │  machine.config
                │  │  settings.map
                │  │  web.config
                │  │
                │  └─Browsers
                │          Compat.browser
                │
                ├─4.0
                │  │  DefaultWsdlHelpGenerator.aspx
                │  │  machine.config
                │  │  settings.map
                │  │  web.config
                │  │
                │  └─Browsers
                │          Compat.browser
                │
                ├─4.5
                │  │  DefaultWsdlHelpGenerator.aspx
                │  │  machine.config
                │  │  settings.map
                │  │  web.config
                │  │
                │  └─Browsers
                │          Compat.browser
                │
                └─mconfig
                        config.xml
```
