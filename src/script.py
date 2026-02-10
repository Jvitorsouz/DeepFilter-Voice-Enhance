from df.io import load_audio, save_audio
from df import enhance, init_df

model, df_state, _ = init_df()

audio_path = "../audio/noisy_snr0.wav"
audio, info = load_audio(audio_path, sr=df_state.sr())

enhanced_audio = enhance(model, df_state, audio)

save_audio("../audio/audio_limpo.wav", enhanced_audio, df_state.sr())

print("Processamento concluído com sucesso!")