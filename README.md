
## Flask API Reference

#### Process Audio

```http
  POST https://komura-audio-process-665606747903.asia-southeast2.run.app/audio/process-audio
```

#### Body
| Field | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `userId` | `string` | **Required**. Current Logged User |
| `audioFile` | `file` | **Required**. Type: MP3 |
| `recordingTitle` | `string` | **Required**. |

#### Response Example
```http
  {
    "firestoreResponse": {
        "data": {
            "audioUrl": "https://storage.googleapis.com/komura-audio-bucket/audio/GJPRRG3ujaM8dXb4G7PAKL96uLp2-1733555874.mp3",
            "confidence": 0.9503234624862671,
            "confidentLabel": 1,
            "createdAt": {},
            "duration": 56.952,
            "fillers_count": 2,
            "pace": "good",
            "recordingTitle": "Nasi goreng enak tau",
            "transcribe": "Hi, my name is Iki. Abud is my brother, and just like my brother, there are 15 million occupational drivers in Indonesia according to the Statistic Agency of Indonesia. The occupational driver face similar challenges to Abud, and some even resort to preying on the sidewalk. The busy environment can be distracting, which can affect their prayers, such as forgetting the number of raka'at, mispronouncing the prayers, or not being able to focus. And also, it is dangerous to pray on the sidewalk. As occupational drivers, they often work long hours, sometimes up to 20 hours a day. This extensive commitment can make it challenging to fulfill the religious obligation of praying five times a day.",
            "word_count": 117,
            "wpm": 123.26169405815425
        },
        "id": "xuTwt82NWEPl4k3MJdtu",
        "message": "Recording created successfully."
    },
    "message": "Audio file processed and saved successfully"
}
```


